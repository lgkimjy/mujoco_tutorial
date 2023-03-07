# CMake minimum version
cmake_minimum_required(VERSION 3.16)
project(
    template_cpp
    DESCRIPTION "Test Project for linking MuJoCo in CPP with CMakeLists."
)

# Options
add_compile_options(-std=c++17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_CXX_FLAGS} -Wl,-no-as-needed")

# Finding Pkgs
find_package(PkgConfig REQUIRED)
find_package(Eigen3 REQUIRED) 
find_package(mujoco REQUIRED) # Follow the instruction _____.md
# Finding GLFW
find_library(GLFW libglfw.so.3 HINTS ${CMAKE_SOURCE_DIR}/lib/glfw-3.3.8)

# Log Message
message(STATUS "PROJECT NAME : " ${PROJECT_NAME})
message(STATUS "GLFW lib found at: " ${GLFW})
message(STATUS "EIGEN DIR : " ${EIGEN3_INCLUDE_DIR})

include_directories(
    include
    INCLUDE_DIRS include
    LIBRARIES ${PROJECT_NAME}
    ${EIGEN3_INCLUDE_DIR}
    DEPENDS system_lib
)

add_executable(${PROJECT_NAME} src/main.cpp src/test.cpp)
target_link_libraries(${PROJECT_NAME} ${GLFW} mujoco::mujoco)