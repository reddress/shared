<?php

$gradient = imagecreate(128, 128);
$gray[] = imagecolorallocate($gradient, 0, 0, 0);

for ($i = 0; $i < 256; $i++) {
    $gray[] = imagecolorallocate($gradient, $i, $i, $i);
}

for ($i = 0; $i < 127; $i++) {
    for ($j = 0; $j < 127; $j++) {
        imagesetpixel($gradient, $i, $j, $gray[$i+$j]);
    }
}

header("Content-type: image/png");
imagepng($gradient);
