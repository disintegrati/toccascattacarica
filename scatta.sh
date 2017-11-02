#/bin/sh 

nome=$(date +%Y-%m-%dT%H-%M-%S)
ext=".jpg"
echo $nome$ext
fswebcam --resolution 1280x720 --no-timestamp --no-info --no-underlay --no-overlay --no-banner ./toupload/$nome$ext
