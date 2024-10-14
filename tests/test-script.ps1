heif-convert image.heic -f jpg -q 90
heif-convert *.heic -f jpg -q 90 -o image-wildcard
heif-convert image.heic -f png

$status_code = 0

$expected_jpg_hash = "3fb5fff1c6bb5f0f5d76d9839f82564d857e81f71e748da1ec480affde10fa8e"
$expected_png_hash = "f6e29566f59bcce7d0486c9745602354cd903da0dbfce3facb8bba476abeee54"

$actual_jpg_hash = (Get-FileHash -Algorithm SHA256 image.jpg).Hash
$actual_jpg_wildcard_hash = (Get-FileHash -Algorithm SHA256 image-wildcard.jpg).Hash

if ($expected_jpg_hash -ne $actual_jpg_hash) {
    Write-Host "JPG image hash differs from expected. Expected: $expected_jpg_hash, Actual: $actual_jpg_hash"
    $status_code = 1
}

if ($expected_jpg_hash -ne $actual_jpg_wildcard_hash) {
    Write-Host "JPG wildcard image hash differs from expected. Expected: $expected_jpg_hash, Actual: $actual_jpg_wildcard_hash"
    $status_code = 1
}

$actual_png_hash = (Get-FileHash -Algorithm SHA256 image.png).Hash

if ($expected_png_hash -ne $actual_png_hash) {
    Write-Host "PNG image hash differs from expected. Expected: $expected_png_hash, Actual: $actual_png_hash"
    $status_code = 1
}

exit $status_code
