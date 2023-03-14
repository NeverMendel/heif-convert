# heif-convert

Multi-Platform command line tool written in Python to convert HEIF images.

## 📝 Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Arguments](#arguments)
- [Libraries](#libraries)
- [Supported operating systems](#supported-operating-systems)
- [License](#license)

## 📕 About <a name="about"></a>

heif-convert is a multi-platform tool written in Python to convert High Efficiency Image File (HEIF) images to jpg, png, webp, gif, tiff, bmp, or ico.

heif-convert is designed to make HEIF batch conversion easy.

## ⚙️ Installation <a name="installation"></a>

## Python repository

The easiest way to get heif-convert is through the pypi.org repository. Install it by running the following command:

```bash
pip install heif-convert
```

## Building from source

To install heif-convert from source, clone this repository and run `pip install .` as follows:

```bash
git clone https://github.com/NeverMendel/heif-convert.git
cd heif-convert
pip install .
```

## Docker image

To pull heif-convert Docker image, run:

```bash
docker pull nevermendel/heif-convert
```

## Usage

heif-convert can be used from the command line by invoking the `heif-convert` command.

Convert an HEIF image to a JPG image:

```bash
heif-convert input.heic -f jpg
```

Convert all HEIF images in the current folder to JPG images:

```bash
heif-convert *.heic -f jpg
```

### Docker image

Convert an HEIF image to PNG using the Docker image:

```bash
docker run -v $(pwd):/usr/app/out --rm nevermendel/heif-convert input.heic -f jpg
```

## Arguments

```
usage: heif-convert [-h] [-o OUTPUT] [-p PATH]
                    [-f {jpg,png,webp,gif,tiff,bmp,ico}] [-q QUALITY] [-v] [-vv]
                    [-V]
                    input [input ...]

Command line tool to convert HEIF images

positional arguments:
  input                 HEIF input file(s)

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file name
                        defaults to original file name (default: '{name}')
  -p PATH, --path PATH  output file path
                        defaults to original file path (default: '{path}')
  -f {jpg,png,webp,gif,tiff,bmp,ico}, --format {jpg,png,webp,gif,tiff,bmp,ico}
                        output format (default: jpg)
  -q QUALITY, --quality QUALITY
                        output quality, integer [0, 100] (default: 90)
  -v, --verbose         enable verbose logging
  -vv, --extra-verbose  enable extra verbose logging
  -V, --version         show program's version number and exit
```

## Libraries

heif-convert uses the following libraries:

- [Pillow](https://github.com/python-pillow/Pillow)
- [pillow_heif](https://github.com/bigcat88/pillow_heif)

## Supported operating systems

heif-convert works on Linux, Mac OS and Windows systems. For further information refer to the [pillow_heif](https://github.com/bigcat88/pillow_heif) repository.

## License

[MIT License](LICENSE)