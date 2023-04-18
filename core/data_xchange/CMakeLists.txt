cmake_minimum_required(VERSION 3.23)
project(data_xchange)

set(CMAKE_CXX_STANDARD 14)
set(TARGET_LOGGER spdlog)
include_directories(.)
include_directories(Thirdparty/spdlog/include)
set(BOOST_INCLUDE_LIBRARIES thread filesystem system program_options)
set(BOOST_ENABLE_CMAKE ON)

include(FetchContent)
FetchContent_Declare(
        Boost
        GIT_REPOSITORY https://github.com/boostorg/boost.git
        GIT_TAG boost-1.80.0
)
FetchContent_MakeAvailable(Boost)
find_package(Protobuf REQUIRED)

add_subdirectory(Thirdparty/pybind11)
include_directories(${Protobuf_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_BINARY_DIR})
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS messages/pub_sub_messages.proto)

add_executable(data_xchange
        main.cpp ${PROTO_SRCS} ${PROTO_HDRS} UserApplication/UserApplication.cpp UserApplication/UserApplication.h Publishers/Publishers.cpp Publishers/Publishers.h Subscribers/Subscribers.cpp Subscribers/Subscribers.h Publishers/Publisher.cpp Publishers/Publisher.h Subscribers/Subscriber.cpp Subscribers/Subscriber.h Messenger/Messenger.cpp Messenger/Messenger.h Topic/Topic.cpp Topic/Topic.h Server/Server.cpp Server/Server.h Server/Request/Request.cpp Server/Request/Request.h)
target_link_libraries(data_xchange ${Protobuf_LIBRARIES} Boost::tokenizer)
add_executable(pub_sub_example ${PROTO_SRCS} ${PROTO_HDRS} Example/pub_sub_example.cpp Example/pub_sub_example.h)
target_link_libraries(pub_sub_example ${Protobuf_LIBRARIES})

pybind11_add_module(posix_message_queue_wrapper PythonWrapper/PosixMessageQueueWrapper.h PythonWrapper/PosixMessageQueueWrapper.cpp PythonWrapper/PythonBindings.cpp ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(posix_message_queue_wrapper PRIVATE ${Protobuf_LIBRARIES})
