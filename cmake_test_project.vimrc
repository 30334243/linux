source ~/.vimrc
let $generate="cmake -DCMAKE_BUILD_TYPE=Release
   \ -DCMAKE_C_COMPILER=/usr/bin/gcc-12
   \ -DCMAKE_CXX_COMPILER=/usr/bin/g++-12
   \ -S /home/zero/cxx/Project
   \ -B /home/zero/cxx/Project-linux"
let $clear="rm -r /home/zero/cxx/Project-linux"
set makeprg=cmake\ --build\ /home/zero/cxx/Project-linux\ -j8
let $cache="ccmake /home/zero/cxx/Project-linux/CMakeCache.txt"
set errorformat^=../%f:%l:%c\ %m
set errorformat^=../../%f:%l:%c\ %m
set errorformat^=../../../%f:%l:%c\ %m
let g:vimspector_break_on_exception = 0
let g:vimspector_terminal_maxwidth = 30
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
nnoremap <silent> <leader>ls : so Session.vim<cr>
nnoremap <silent>,cb : make!<cr>
nnoremap <silent>,cd : !exec $clear<cr>
nnoremap <silent>,cg : !exec $generate<cr>
nnoremap <silent>,cc : !exec $generate<cr>
nnoremap <silent>,cr : !exec /home/zero/cxx/Project-linux/bin/Release/srvgrid -c /home/zero/Documents&<cr>
nnoremap <silent>,ck : !exec pkill Project<cr>
let g:vimspector_configurations = {
\		"attach": {
\			"adapter": "vscode-cpptools", 
\			"variables": {
\				"pid": {
\					"shell": [
\						"/bin/bash",
\						"-c",
\						"pgrep Project | sort | tail -1"
\					]
\				}
\			},
\			"configuration": {
\				"request": "attach",
\				"program": "/home/zero/cxx/Project-linux/bin/Debug/Project",
\           "cwd":"/home/zero/cxx/Project-linux/bin/Debug",
\           "environment":[],
\           "processId":"$pid",
\				"MIMode": "gdb",
\				"setupCommands":[
\						{"text":"-enable-pretty-printing","ignoreFailures":"false"},
\                  {"text":"set disassembly-flavor intel","ignoreFailures":"false"}
\				]
\         }
\         }
\	}
