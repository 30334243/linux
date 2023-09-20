import os
import sys
import pwd
import MyColor as Color
# python vimrc_create.py
# 1.  name-vimrc
# 2.  debug
# 3.  compiler
# 4.  version-compiler
# 5.  name-project
# 6.  type-build
# 7.  num-cores
# 8.  path-source
# 9.  path-build
# 10. args
# example
print(Color.GREEN+"Example:")
print(Color.PURPLE+"python "+Color.GREEN+"vimrc_create.py\n"+
      Color.YELLOW+"\t.vimrc "+Color.RED+"(name config .vimrc)\n"+
      Color.YELLOW+"\tdebug "+Color.RED+"(launch or attach)\n"+
      Color.YELLOW+"\tgcc "+Color.RED+"(compiler)\n"+
      Color.YELLOW+"\t12 "+Color.RED+"(version compiler)\n"+
      Color.YELLOW+"\tProject "+Color.RED+"(name project)\n"+
      Color.YELLOW+"\tRelease "+Color.RED+"(build type)\n"+
      Color.YELLOW+"\t8 "+Color.RED+"(cores)\n"+
      Color.YELLOW+"\t/home/zero/cxx/Project "+Color.RED+"(path project)\n"+
      Color.YELLOW+"\t/home/zero/cxx/Project-linux "+Color.RED+"(path build)\n"+
      Color.YELLOW+"\t\"-c /home/zero/Documents\" "+Color.RED+"(argumets)"+Color.END)
args = sys.argv
if args.__len__() <= 1:
    exit()
name_vimrc       = args[1]
file = open(name_vimrc,"w+")
debug         = args[2]
compiler         = args[3]
version_compiler = args[4]
name_project     = args[5]
type_build       = args[6]
num_cores        = args[7]
path_source      = args[8]
path_build       = args[9]
args             = args[10]
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
if debug == "launch":
    file.write('\		"launch": {\n')
    file.write('\			"adapter": "vscode-cpptools", \n')
    file.write('\			"configuration": {\n')
    file.write('\				"request": "launch",\n')
    file.write(f'\				"program": "{path_build}/{name_project}",\n')
    file.write(f'\           "cwd":"{path_build}",\n')
    file.write('\           "environment":[],\n')
    file.write('\				"MIMode": "gdb",\n')
    file.write('\				"setupCommands":[\n')
    file.write('\						{"text":"-enable-pretty-printing","ignoreFailures":"false"},\n')
    file.write('\                  {"text":"set disassembly-flavor intel","ignoreFailures":"false"}\n')
    file.write('\				]\n')
    file.write('\         }\n')
    file.write('\         }\n')
    file.write('\	}\n')
elif debug == "attach":
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
    file.write(f'\				"program": "{path_build}/Debug/{name_project}",\n')
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
else:
    print(Color.RED+"debug error \""+debug+"\""+Color.END)
