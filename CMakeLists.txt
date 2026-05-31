cmake_minimum_required(VERSION 3.10)
project(real-esrgan-upscaler-tool)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)
find_package(OpenCV REQUIRED)

add_executable(${PROJECT_NAME}
    src/main.cpp
    src/mainwindow.cpp
    src/imageprocessor.cpp
    src/upscaler.cpp
)

target_link_libraries(${PROJECT_NAME}
    Qt6::Widgets
    ${OpenCV_LIBS}
)