cmake_minimum_required(VERSION 3.5)
project(temp)

# Set the output directory for executables
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/bin)

# Add a target for each day's solution
add_executable(day01 day01/main.cpp Helpers/file_utils.cpp)
add_executable(day02 day02/main.cpp Helpers/file_utils.cpp)

# Include the Helpers directory for header files
include_directories(Helpers)

# Optionally set C++ standard (for example, C++17)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)