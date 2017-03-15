<?php

$img_input  = $_POST['photo-data'];
$img_string = base64_decode(explode(',', $img_input)[1]);
$img        = imagecreatefromstring($img_string);

header('Content-type: image/png');
imagepng($img);