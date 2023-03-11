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
        "--folder", type=str, default=".", help="working directory (default: '.')"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="{name}",
        help="output file name excluding its extension\n"
        + "defaults to original file name (default: '{name}')",
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
        input_filepath = os.path.join(args.folder, input_file)
        if not os.path.isfile(input_filepath):
            parser.error(f"Input file '{input_filepath}' does not exist")

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

    if not os.path.isdir(args.folder):
        logging.info("Output folder not found, creating it")
        os.mkdir(args.folder)
    os.chdir(args.folder)

    for input_file in args.input:
        logging.info(f"Reading {input_file}")
        image = Image.open(input_file)
        output_filename = (
            args.output.format(name=input_file.split(".")[0]) + "." + args.format
        )
        output_filepath = os.path.join(output_filename)
        logging.info(f"Writing {output_filepath}")
        image.save(output_filepath, quality=args.quality)
        print(f"Wrote {output_filepath}")


if __name__ == "__main__":
    main()
