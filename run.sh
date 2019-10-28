#!/bin/bash

xhost +

docker run --rm -it \
	-v /etc/localtime:/etc/localtime:ro \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-v /usr/share/X11/xkb:/usr/share/X11/xkb:ro \
	-e DISPLAY=$DISPLAY \
	--device /dev/video0 \
	-v /home/marcelo/Code/ma/opencv/:/app \
	valian/docker-python-opencv-ffmpeg:py3 \
	python3 /app/$@
