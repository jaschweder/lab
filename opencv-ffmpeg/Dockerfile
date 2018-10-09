FROM ubuntu:17.04

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y \
    git \
    build-essential \
    cmake \
    pkg-config \
    yasm \
    libx264-dev

#install FFMPEG
RUN mkdir -p /usr/src \
    && cd /usr/src \
    && git clone -b n3.2.7 --depth 1 --single-branch https://github.com/ffmpeg/ffmpeg \
    && cd ffmpeg \
    && ./configure \
    --enable-gpl \
    --enable-libx264 \
    --enable-shared \
    --disable-static \
    && make all -j$(nproc) \
    && make install \
    && cd /usr/local/include/ \
    && ln -s libavcodec/avcodec.h avcodec.h \
    && ln -s libavformat/avformat.h avformat.h \
    && ln -s libavio/avio.h avio.h \
    && ln -s libavutil/avutil.h avutil.h \
    && ln -s libswscale/swscale.h swscale.h

ENV PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

##install OpenCV
RUN cd /usr/src \
    && git clone -b 3.2.0 --depth 1 --single-branch https://github.com/opencv/opencv \
    && cd opencv \
    && mkdir build \
    && cd build \
    && cmake \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D BUILD_DOXYGEN_DOCS=OFF \
    -D CMAKE_VERBOSE=ON \
    -D BUILD_NEW_PYTHON_SUPPORT=OFF \
    -D BUILD_PYTHON_SUPPORT=OFF \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_SHARED_LIBS=ON \
    -D ENABLE_SSE=ON \
    -D ENABLE_SSE2=ON \
    -D ENABLE_SSE3=ON \
    -D OPENCV_BUILD_3RDPARTY_LIBS=ON \
    -D USE_O3=ON \
    -D USE_OMIT_FRAME_POINTER=ON \
    -D WITH_FFMPEG=ON \
    -D WITH_PNG=OFF \
    -D WITH_V4L=ON \
    -D WITH_LIBV4L=ON \
    .. \
    && make -j$(nproc) \
    && make install
