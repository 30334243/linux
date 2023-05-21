#!/bin/bash
echo -n "Enter path project: "
read path_project
cd $path_project
git clone https://github.com/google/googletest.git
echo -n "Enter project name: "
read name_project
touch $name_project.hpp
touch main.cpp
echo '#include "googletest/googletest/include/gtest/gtest.h"
int main(int argc, char **argv) {
   ::testing::InitGoogleTest(&argc, argv);
   return RUN_ALL_TESTS();
}' > main.cpp
# CMAKELISTS.TXT
touch CMakeLists.txt
echo "cmake_minimum_required(VERSION 3.22)
project($name_project)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(SRC
   main.cpp
   $name_project.hpp
   )
add_subdirectory(./googletest gtest)
add_executable(\${PROJECT_NAME} \${SRC})
target_link_libraries(\${PROJECT_NAME} PRIVATE gtest_main)
add_custom_command(TARGET \${PROJECT_NAME} POST_BUILD
   COMMAND \${CMAKE_COMMAND} -E copy \${CMAKE_BINARY_DIR}/compile_commands.json \${CMAKE_SOURCE_DIR}/compile_commands.json
   )
" > CMakeLists.txt
# VIMRC
touch .vimrc
echo 'source ~/.vimrc
' > .vimrc
# COMPILER
echo -n "Enter compiler (clang=1 or gcc=2): "
read compiler
if [[ $compiler == "1" || $compiler == "2" ]]
then
   # VERSION COMPILER
   echo -n "Enter version compiler: "
   read version_compiler
   if [[ $compiler == "1" ]]
   then
      echo "let \$generate=\"cmake -DCMAKE_BUILD_TYPE=Debug -DCMAKE_C_COMPILER=/usr/bin/clang-$version_compiler -DCMAKE_CXX_COMPILER=/usr/bin/clang++-$version_compiler -S $path_project -B $path_project-linux\"
      " >> .vimrc
   elif [[ $compiler == "2" ]]
   then
      echo "let \$generate=\"cmake -DCMAKE_BUILD_TYPE=Debug -DCMAKE_C_COMPILER=/usr/bin/gcc-$version_compiler -DCMAKE_CXX_COMPILER=/usr/bin/g++-$version_compiler -S $path_project -B $path_project-linux\"
      " >> .vimrc
   fi
   echo "let \$clear=\"rm -r $path_project-linux\"
   set makeprg=cmake\ --build\ $path_project-linux\ -j4
   set errorformat=\%E\%f\:\%l\:\%c\:\ \%trror:\ \%m,\%-C,\%-Z\%p\^
   set errorformat+=\%D\%\*\\\a\:\ Entering\ directory\ \[\`\'\]\%f\'
   set errorformat+=\%X\%\*\\\a\:\ Leaving\ directory\ \[\`\'\]\%f\'
   set errorformat+=\%-G\%\.\%\#" >> .vimrc
   # DEBUG MODE
   echo -n "Enter debug mode (launch=1 or attach=2): "
   read debug_mode
   if [[ $debug_mode == "1" || $debug_mode == "2" ]]
   then
      # DEBUG
      echo 'let g:vimspector_break_on_exception = 0
      let g:vimspector_terminal_maxwidth = 40
      let g:vimspector_code_minwidth = 100
      nnoremap <silent> <leader>vc : call vimspector#Continue()<cr>
      nnoremap <silent> <leader>vl : call vimspector#Launch()<cr>
      nnoremap <silent> <leader>vr : call vimspector#Reset()<cr>
      nnoremap <silent> <c-s> : call vimspector#StepSOver()<cr>
      nnoremap <silent> <leader>si : call vimspector#StepSInto()<cr>
      nnoremap <silent> <leader>sd : call vimspector#ShowDisassambly()<cr>
      nnoremap <silent> <leader>b : call vimspector#ToggleBreakpoint()<cr>
      nnoremap <silent> <leader>vi <Plug>VimspectorBalloonEval<cr>
      nnoremap <silent> <leader>u : call vimspector#UpFrame()<cr>
      nnoremap <silent> <leader>d : call vimspector#DownFrame()<cr>
      nnoremap <silent> <leader>lb : call vimspector#ListBreakpoints()<cr>
      nnoremap <silent> <leader>rc : call vimspector#RunToCursor()<cr>
      ' >> .vimrc
      if [[ $debug_mode == "1" ]]
      then
         echo "let g:vimspector_configurations = {
         \		\"launch\": {
         \			\"adapter\": \"vscode-cpptools\", 
         \			\"configuration\": {
         \				\"request\": \"launch\",
         \				\"program\": \"$path_project-linux/$name_project\",
         \           \"cwd\":\"$path_project-linux\",
         \           \"environment\":[],
         \				\"MIMode\": \"gdb\",
         \				\"setupCommands\":[
         \						{\"text\":\"-enable-pretty-printing\",\"ignoreFailures\":\"false\"},
         \                  {\"text\":\"set disassembly-flavor intel\",\"ignoreFailures\":\"false\"}
         \				]
         \         }
         \         }
         \	}
         " >> .vimrc
      elif [[ $debug_mode == "2" ]]
      then
         echo "let g:vimspector_configurations = {
         \		\"attach\": {
         \			\"adapter\": \"vscode-cpptools\", 
         \			\"variables\": {
         \				\"pid\": {
         \					\"shell\": [
         \						\"/bin/bash\",
         \						\"-c\",
         \						\"pgrep $name_project | sort | tail -1\"
         \					]
         \				}
         \			},
         \			\"configuration\": {
         \				\"request\": \"attach\",
         \				\"program\": \"$path_project-linux/$name_project\",
         \           \"cwd\":\"$path_project\",
         \           \"environment\":[],
         \           \"processId\":\"\${pid}\",
         \				\"MIMode\": \"gdb\",
         \				\"setupCommands\":[
         \						{\"text\":\"-enable-pretty-printing\",\"ignoreFailures\":\"false\"},
         \                  {\"text\":\"set disassembly-flavor intel\",\"ignoreFailures\":\"false\"}
         \				]
         \         }
         \         }
         \	}
         " >> .vimrc
      else
         echo "error: argument $debug_mode must die \"launch or attach\""
      fi
   fi
fi
echo "nnoremap <silent> <leader>ls : so Session.vim<cr>
nnoremap <silent>,cb : make!<cr>
nnoremap <silent>,cd : !exec \$clear<cr>
nnoremap <silent>,cg : !exec \$generate<cr>
nnoremap <silent>,cr : !exec $path_project-linux/$name_project<cr>
" >> .vimrc
