FROM golang

RUN apt-get update -y \
    && apt-get install -y \
        build-essential \
        git \
        libpcre3-dev \
        autoconf \
        automake \
        libtool \
        bison \
        libboost-dev

RUN mkdir -p /usr/src \
    && git clone --single-branch --depth 1 https://github.com/swig/swig /usr/src/swig \
    && cd /usr/src/swig \
    && ./autogen.sh \
    && mkdir -p build/build \
    && cd build/build \
    && ../../configure \
    && make -j$(nproc) \
    && make install
