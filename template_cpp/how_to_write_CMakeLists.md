<!-- ---
# marp: true
marp: false
backgroundColor: #fff
paginate: true
--- -->

## How to write CMakeLists.txt with using mujoco

---

### Make a personal project directory.
```bash
$ mkdir PROJECT_NAME 
```

---
### Clone needed library ( mujoco )
1. Make a library folder

    ```bash
    $ mkdir lib src include
    ```
2. Clone deepmind/mujoco repository in PROJECT lib folder.
3. Make a build directory in mujoco repository, ```mkdir build```.
4. Dive in to build dir, 

    ```bash
    $ cmake ..
    $ make -j
    $ cmake --install .
    ```

---

### Directory Structure
```
PROJECT_NAME/
├── CMakeLists.txt
├── README.md
├── lib
│   ├── mujoco
│   └── glfw
├── include
│   ├── test1.hpp
│   └── test2.hpp
└── src
    ├── test1.cpp
    ├── test2.cpp
    └── main.cpp    
```
---

### HOW To Build MuJoCo using CMakeLists.txt
1. Write a CMakeLists.txt
    ```CMake
    find_package(mujoco)
    target_link_libraries(${PROJECT_NAME} mujoco::mujoco)
    ```

2. Make build directory, and ```cmake ..```, ```make``` in build directory.
3. Then, you have just made an executable file to run.

---



### Example of Full CMakeLists.txt
```Cmake
cmake_minimum_required(VERSION 3.1)
project(mujoco_test)
add_definitions(-std=c++17)

find_package(mujoco)
find_package(glfw3)

add_executable(${PROJECT_NAME} src/main.cpp src/test1.cpp src/test2.cpp)
target_link_libraries(${PROJECT_NAME} mujoco::mujoco glfw)
```

---
### Code start like this

```C++
#include <iostream>

#include <GLFW/glfw3.h>
#include <mujoco/mujoco.h>

using namespace std;

int main()
{
    return 0;
}
```