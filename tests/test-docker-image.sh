#!/bin/bash

docker run -v "$(pwd)":/usr/app/out --rm nevermendel/heif-convert image.heic -f jpg -q 90 -o result
docker run -v "$(pwd)":/usr/app/out --rm nevermendel/heif-convert image.heic -f png -o result

status_code=0

if ! cmp -s image.jpg result.jpg; then
  echo "jpg image is different"
  status_code=1
fi

if ! cmp -s image.png result.png; then
  echo "png image is different"
  status_code=1
fi

exit $status_code
