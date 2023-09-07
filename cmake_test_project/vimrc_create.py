import os
import sys
import pwd
# python vimrc_create.py
# 1. name-vimrc
# 2. compiler
# 3. version-compiler
# 4. name-project
# 5. type-build
# 6. num-cores
# 7. path-source
# 8. path-build
# 9. args
# example
# >python vimrc_create.py .vimrc gcc 12 Project Release 8
#                         /home/zero/cxx/Project
#                         /home/zero/cxx/Project-linux
#                         -c /home/zero/Documents
args = sys.argv
name_vimrc       = args[1]
file = open(name_vimrc,"w+")
compiler         = args[2]
version_compiler = args[3]
name_project     = args[4]
type_build       = args[5]
num_cores        = args[6]
path_source      = args[7]
path_build       = args[8]
args             = args[9]
compiler_cpp = ""
if compiler == "gcc":
    compiler_cpp = "g++"
if compiler == "clang":
    compiler_cpp = "clang++"
file.write('source ~/.vimrc\n')
file.write(f'let $generate="cmake -DCMAKE_BUILD_TYPE={type_build}\n')
file.write(f'   \ -DCMAKE_C_COMPILER=/usr/bin/{compiler}-{version_compiler}\n')
file.write(f'   \ -DCMAKE_CXX_COMPILER=/usr/bin/{compiler_cpp}-{version_compiler}\n')
file.write(f'   \ -S {path_source}\n')
file.write(f'   \ -B {path_build}"\n')
file.write(f'let $clear="rm -r {path_build}"\n')
file.write(f'set makeprg=cmake\ --build\ {path_build}\ -j{num_cores}\n')
file.write(f'let $cache=\"ccmake {path_build}/CMakeCache.txt"\n')
file.write('set errorformat^=../%f:%l:%c\ %m\n')
file.write('set errorformat^=../../%f:%l:%c\ %m\n')
file.write('set errorformat^=../../../%f:%l:%c\ %m\n')
file.write('let g:vimspector_break_on_exception = 0\n')
file.write('let g:vimspector_terminal_maxwidth = 30\n')
file.write('let g:vimspector_code_minwidth = 100\n')
file.write('nnoremap <silent> <leader>vc : call vimspector#Continue()<cr>\n')
file.write('nnoremap <silent> <leader>vl : call vimspector#Launch()<cr>\n')
file.write('nnoremap <silent> <leader>vr : call vimspector#Reset()<cr>\n')
file.write('nnoremap <silent> <c-s> : call vimspector#StepSOver()<cr>\n')
file.write('nnoremap <silent> <leader>si : call vimspector#StepSInto()<cr>\n')
file.write('nnoremap <silent> <leader>sd : call vimspector#ShowDisassambly()<cr>\n')
file.write('nnoremap <silent> <leader>b : call vimspector#ToggleBreakpoint()<cr>\n')
file.write('nnoremap <silent> <leader>vi <Plug>VimspectorBalloonEval<cr>\n')
file.write('nnoremap <silent> <leader>u : call vimspector#UpFrame()<cr>\n')
file.write('nnoremap <silent> <leader>d : call vimspector#DownFrame()<cr>\n')
file.write('nnoremap <silent> <leader>lb : call vimspector#ListBreakpoints()<cr>\n')
file.write('nnoremap <silent> <leader>rc : call vimspector#RunToCursor()<cr>\n')
file.write('nnoremap <silent> <leader>ls : so Session.vim<cr>\n')
file.write('nnoremap <silent>,cb : make!<cr>\n')
file.write('nnoremap <silent>,cd : !exec $clear<cr>\n')
file.write('nnoremap <silent>,cg : !exec $generate<cr>\n')
file.write('nnoremap <silent>,cc : !exec $cache<cr>\n')
file.write(f'nnoremap <silent>,cr : !exec {path_build}/{name_project} {args}&<cr>\n')
file.write(f'nnoremap <silent>,ck : !exec pkill {name_project}<cr>\n')
file.write('let g:vimspector_configurations = {\n')
file.write('\		"attach": {\n')
file.write('\			"adapter": "vscode-cpptools", \n')
file.write('\			"variables": {\n')
file.write('\				"pid": {\n')
file.write('\					"shell": [\n')
file.write('\						"/bin/bash",\n')
file.write('\						"-c",\n')
file.write(f'\						"pgrep {name_project} | sort | tail -1"\n')
file.write('\					]\n')
file.write('\				}\n')
file.write('\			},\n')
file.write('\			"configuration": {\n')
file.write('\				"request": "attach",\n')
file.write(f'\				"program": "{path_build}/bin/Debug/{name_project}",\n')
file.write(f'\           "cwd":"{path_build}/bin/Debug",\n')
file.write('\           "environment":[],\n')
file.write('\           "processId":"$pid",\n')
file.write('\				"MIMode": "gdb",\n')
file.write('\				"setupCommands":[\n')
file.write('\						{"text":"-enable-pretty-printing","ignoreFailures":"false"},\n')
file.write('\                  {"text":"set disassembly-flavor intel","ignoreFailures":"false"}\n')
file.write('\				]\n')
file.write('\         }\n')
file.write('\         }\n')
file.write('\	}\n')
