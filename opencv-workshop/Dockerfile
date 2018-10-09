FROM jaschweder/php:server

MAINTAINER jonathanschweder@gmail.com

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y \
    git \
    build-essential \
    cmake

RUN cd /usr/src \
    && git clone -b 2.4 --depth 1 --single-branch https://github.com/opencv/opencv \
    && cd opencv \
    && mkdir build \
    && cd build \
    && cmake \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D BUILD_DOXYGEN_DOCS=OFF \
    -D CMAKE_VERBOSE=OFF \
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
    -D WITH_PNG=ON \
    -D WITH_LIBV4L=ON \
    .. \
    && make -j$(nproc) \
    && make install
