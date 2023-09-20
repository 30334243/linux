import os
import sys
import subprocess
import MyGit as Git
import MyWriteMain as Main
import MyColor as Color

def GetVersion():
    res = subprocess.run(["cmake","-version"],
                          capture_output=True,
                          text=True)
    res = res.stdout
    cmake_version = 0
    if res != "":
        idx = res.find("cmake version ")
        return str(res[idx+14:idx+14+4])
# 1. name-project
# . cmake-version
# . qt
# . gprof
# . googletest
# . benchmark
# . sfml
def CreateCMakeLists(project_path,name_project,args):
    print(Color.GREEN+"Example:")
    print(Color.PURPLE+"  1. python "+Color.GREEN +"MyCMakeListCreat.py "+
          Color.YELLOW+"Project 3.22 "+Color.END)
    print(Color.PURPLE+"  2. python "+Color.GREEN +"MyCMakeListCreat.py "+
          Color.YELLOW+"Project 3.22 "+
          Color.LIGHT_PURPLE+"qt gprof googletest benchmark"+Color.END)
    print(Color.PURPLE+"  2. python "+Color.GREEN +"MyCMakeListCreat.py "+
          Color.YELLOW+"Project 3.22 "+Color.LIGHT_PURPLE+"qt gprof "
          "googletest=/home/zero/cxx/include/googletest "
          "benchmark=/home/zero/cxx/include/benchmark"+Color.END)
    # args = sys.argv
    if args.__len__() < 1:
        print(Color.RED+"Не достаточно аргументов"+Color.END)
        exit()
    cmake = open("CMakeLists.txt","w+")
    name_project = args[0]
    qt = False
    gprof = False
    googletest = False
    benchmark = False
    sfml = False
    path_googletest = "."
    path_benchmark = "."
    path_sfml = "."
    cmake_version = ""
    print(Color.GREEN+"Current version CMake: "+GetVersion()+Color.END+"\n")
    for arg in args[1:]:
        if arg == "qt":
            qt = True
        if arg == "gprof":
            gprof = True
        if arg == "googletest":
            googletest = True
        elif arg.startswith("googletest="):
            path_googletest = arg.removeprefix("googletest=")
            googletest = True
        if arg == "benchmark":
            path_benchmark = arg.removeprefix("googletest=")
            benchmark = True
        if arg == "sfml":
            sfml = True
        if arg.startswith("cmake-version="):
            cmake_version = arg.removeprefix("cmake-version=")
    cmake.write(f'cmake_minimum_required(VERSION {cmake_version})\n')
    cmake.write(f'project({name_project})\n')
    cmake.write('set(CMAKE_CXX_STANDARD 17)\n')
    cmake.write('if (CMAKE_CXX_COMPILER_ID MATCHES "(Clang|GNU)")\n')
    cmake.write('  add_compile_options(-Wall -Wpedantic -Wextra -Werror)\n')
    cmake.write('  add_compile_options(-fsanitize=address -fsanitize=undefined -fno-omit-frame-pointer)\n')
    cmake.write('  add_link_options(-fsanitize=address -fsanitize=undefined -fno-omit-frame-pointer)\n')
    cmake.write('elseif (CMAKE_CXX_COMPILER_ID MATCHES "MSVC")\n')
    cmake.write('    message("Must die")\n')
    cmake.write('endif()\n')
    if gprof:
        cmake.write('#gprof\n')
        cmake.write('SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pg")\n')
        cmake.write('SET(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -pg")\n')
        cmake.write('SET(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -pg")\n\n')
    cmake.write('set(SRC\n')
    cmake.write('   main.cpp\n')
    cmake.write(')\n')
    if qt:
        cmake.write('#qt\n')
        cmake.write('set(CMAKE_AUTOMOC ON)\n')
        cmake.write('set(CMAKE_AUTORCC ON)\n')
        cmake.write('set(CMAKE_AUTOUIC ON)\n')
        cmake.write('find_package(Qt5 REQUIRED COMPONENTS Core)\n')
        cmake.write('#end qt\n')
    if googletest:
        cmake.write('#googletest\n')
        cmake.write(f'add_subdirectory({path_googletest}/googletest)\n')
        cmake.write('#end googletest\n')
        if os.path.exists("googletest") == False:
            Git.CmakeBuild("https://github.com/google/googletest.git")
            if benchmark == False:
                Main.Googletest()
    if benchmark:
        cmake.write('#benchmark\n')
        cmake.write(f'add_subdirectory({path_benchmark}benchmark)\n')
        cmake.write('#end benchmark\n')
        if os.path.exists("benchmark") == False:
            Git.Benchmark()
            Main.Benchmark(googletest)
    cmake.write('add_executable(${PROJECT_NAME} ${SRC})\n')
    if googletest:
        cmake.write('#googletest\n')
        cmake.write('target_link_libraries(${PROJECT_NAME} PRIVATE gtest_main)\n')
        cmake.write('target_include_directories(${PROJECT_NAME} PUBLIC\n')
        cmake.write('                           ${PROJECT_SOURCE_DIR}/googletest/googletest/include\n')
        cmake.write('#end googletest\n')
    if benchmark:
        cmake.write('#benchmark\n')
        cmake.write('target_link_libraries(${PROJECT_NAME} PRIVATE benchmark::benchmark)\n')
        cmake.write('target_include_directories(${PROJECT_NAME} PUBLIC\n')
        cmake.write('                           ${PROJECT_SOURCE_DIR}/benchmark/include\n')
        cmake.write('#end benchmark\n')
    if sfml:
        cmake.write('#sfml\n')
        cmake.write('target_link_libraries(${PROJECT_NAME}\n'
                    '       sfml-graphics'
                    '       sfml-window'
                    '       sfml-system'
                    '       )'
                    )
