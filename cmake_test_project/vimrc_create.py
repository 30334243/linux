import os
import sys

args = sys.argv
name = args[1]
file = open(name,"w+")

# python vimrc_create.py .vimrc gcc 12 Release /home/zero/cxx/grid /home/zero/cxx/grid-linux num
# cores
compiler = args[2]
version_compiler = " " if args[3] == "non" else "-"+args[3]+" "
compiler_cpp = ""
if compiler == "gcc":
    compiler_cpp = "g++"
if compiler == "clang":
    compiler_cpp = "clang++"
path_build = args[5]
file.write("source ~/.vimrc\n"
           f"let $generate=\"cmake -DCMAKE_BUILD_TYPE={args[4]}"
           "-DCMAKE_C_COMPILER=/usr/bin/{compiler}{version_compiler}"
           "-DCMAKE_CXX_COMPILER=/usr/bin/{compiler_cpp}{version_compiler}"
           "-S /home/zero/cxx/grid/"
           "-B {path_build}\n"
           "let $clear=\"rm -r {path_build}\""
           "set makeprg=cmake\ --build\ {path_build}\ -j{num_cores}"
           .format(compiler=compiler,
                   version_compiler=version_compiler,
                   compiler_cpp=compiler_cpp,
                   path_build=path_build
                   )
           );
