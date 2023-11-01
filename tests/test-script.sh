#!/bin/bash

heif-convert image.heic -f jpg -q 90
heif-convert image.heic -f png

status_code=0

expected_jpg_hash="3fb5fff1c6bb5f0f5d76d9839f82564d857e81f71e748da1ec480affde10fa8e"
actual_jpg_hash=$(sha256sum image.jpg | awk '{print $1}')

if [ "$expected_jpg_hash" != "$actual_jpg_hash" ]; then
  echo "JPG image hash differs from expected. Expected: ${expected_jpg_hash}, Actual: ${actual_jpg_hash}"
  status_code=1
fi

expected_png_hash="f6e29566f59bcce7d0486c9745602354cd903da0dbfce3facb8bba476abeee54"
actual_png_hash=$(sha256sum image.png | awk '{print $1}')

if [ "$expected_png_hash" != "$actual_png_hash" ]; then
  echo "PNG image hash differs from expected. Expected: ${expected_png_hash}, Actual: ${actual_png_hash}"
  status_code=1
fi

exit $status_code
