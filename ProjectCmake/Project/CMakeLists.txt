cmake_minimum_required(VERSION )
project(Project)
set(CMAKE_CXX_STANDARD 17)
if (CMAKE_CXX_COMPILER_ID MATCHES "(Clang|GNU)")
  add_compile_options(-Wall -Wpedantic -Wextra -Werror)
  add_compile_options(-fsanitize=address -fsanitize=undefined -fno-omit-frame-pointer)
  add_link_options(-fsanitize=address -fsanitize=undefined -fno-omit-frame-pointer)
elseif (CMAKE_CXX_COMPILER_ID MATCHES "MSVC")
    message("Must die")
endif()
set(SRC
   main.cpp
)
add_executable(${PROJECT_NAME} ${SRC})
