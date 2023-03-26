cmake_minimum_required(VERSION 3.23)
project(data_xchange)

set(CMAKE_CXX_STANDARD 14)

find_package(Protobuf REQUIRED)
include_directories(${Protobuf_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_BINARY_DIR})
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS messages/pub_sub_messages.proto)

add_executable(data_xchange
        main.cpp ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(data_xchange ${Protobuf_LIBRARIES})
