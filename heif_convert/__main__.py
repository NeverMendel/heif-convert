import argparse
import os
import logging
from heif_convert._version import __version__

from PIL import Image
from pillow_heif import register_heif_opener


def parse_args():
    parser = argparse.ArgumentParser(
        description="Command line tool to convert HEIF images",
        formatter_class=lambda prog: argparse.RawTextHelpFormatter(
            "heif-convert", width=80
        ),
    )
    parser.add_argument("input", type=str, nargs="+", help="HEIF input file(s)")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="{name}",
        help="output file name\n"
        + "defaults to original file name (default: '{name}')",
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        default="{path}",
        help="output file path\n"
        + "defaults to original file path (default: '{path}')",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        help="output format (default: jpg)",
        default="jpg",
        choices=["jpg", "png", "webp", "gif", "tiff", "bmp", "ico"],
    )
    parser.add_argument(
        "-q",
        "--quality",
        type=int,
        help="output quality, integer [0, 100] (default: 90)",
        default=90,
    )
    parser.add_argument(
        "-n",
        "--no-metadata",
        dest="metadata",
        action="store_false",
        help="disable conversion of the Exif metadata",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="enable verbose logging",
    )
    parser.add_argument(
        "-vv",
        "--extra-verbose",
        dest="extra_verbose",
        action="store_true",
        help="enable extra verbose logging",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )

    args = parser.parse_args()

    for input_file in args.input:
        if not os.path.isfile(input_file):
            parser.error(f"Input file '{input_file}' does not exist")

    return args


def configure_logging(args):
    logging_stream_handler = logging.StreamHandler()

    # Set stream logging level based on program arguments
    logging_stream_handler.setLevel(logging.WARNING)
    if args.verbose:
        logging_stream_handler.setLevel(logging.INFO)
    if args.extra_verbose:
        logging_stream_handler.setLevel(logging.DEBUG)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s",
        handlers=[logging_stream_handler],
    )


def main():
    args = parse_args()
    configure_logging(args)

    logging.debug(f"heif-convert {__version__} run with arguments: {args}")

    logging.debug("Registering HEIF opener")
    register_heif_opener()

    for input_file in args.input:
        logging.info(f"Reading {os.path.abspath(input_file)}")
        image = Image.open(input_file)
        output_filename = (
            args.output.format(
                name=os.path.splitext(os.path.basename(input_file))[0],
            )
            + "."
            + args.format
        )
        output_filepath = os.path.join(
            args.path.format(
                path=os.path.dirname(os.path.abspath(input_file)),
            ),
            output_filename,
        )
        logging.info(f"Writing {output_filepath}")
        exif_data = None
        if args.metadata:
            exif_data = image.getexif()
        image.save(output_filepath, quality=args.quality, exif=exif_data)
        print(f"Wrote {output_filepath}")


if __name__ == "__main__":
    main()
