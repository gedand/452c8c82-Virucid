cmake_minimum_required(VERSION 3.10)

project(parser)

set(CMAKE_CXX_STANDARD 11)

list(APPEND SRC_FILES 
        main.cpp
        CAFFParser.cpp
        CIFFParser.cpp
        CustomByteArray.cpp)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})

add_executable(parser ${SRC_FILES})
