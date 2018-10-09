#!/bin/bash

gst-launch-1.0 \
    v4l2src device=/dev/video8 ! videoconvert ! videoscale ! video/x-raw,format=I420,width=320,height=240,framerate=10/1 ! \
    videomixer name=mix \
    sink_0::xpos=0   sink_0::ypos=0 \
    sink_1::xpos=320   sink_1::ypos=0 \
    ! jpegenc ! rtpjpegpay ! udpsink host=0.0.0.0 port=5001 auto-multicast=true \
    v4l2src device=/dev/video6 ! videoconvert ! videoscale ! video/x-raw,format=I420,width=320,height=240,framerate=10/1 ! mix.sink_1
