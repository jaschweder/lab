#!/bin/sh

gst-launch-1.0 -e \
    # pipeline, input = /dev/video0, output = http://127.0.0.1:8080
    v4l2src device=/dev/video0 \
        ! videoconvert ! videoscale ! video/x-raw,width=640,height=480 \
        ! theoraenc bitrate=128 ! oggmux ! tcpserversink host=127.0.0.1 port=8080 \

    # pipeline, input = /dev/video1, output = http://127.0.0.1:8081
    v4l2src device=/dev/video1 \
        ! videoconvert ! videoscale ! video/x-raw,width=640,height=480 \
        ! theoraenc bitrate=128 ! oggmux ! tcpserversink host=127.0.0.1 port=8081
