cmake_minimum_required(VERSION 2.8)

project( FaceRecognizer )
find_package( OpenCV REQUIRED )

add_executable( facerecognize facerecognize.cpp )
target_link_libraries( facerecognize ${OpenCV_LIBS} )
target_compile_features(facerecognize PRIVATE cxx_range_for)

add_executable( facedata facedata.cpp )
target_link_libraries( facedata ${OpenCV_LIBS} )
target_compile_features(facedata PRIVATE cxx_range_for)

install(TARGETS facerecognize DESTINATION bin)
install(TARGETS facedata DESTINATION bin)
