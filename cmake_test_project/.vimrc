source ~/.vimrc
<<<<<<< HEAD

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

      let g:vimspector_configurations = {
      \		"configurations": {
      \			"adapter": "debugpy", 
      \        "filetype":["python"],
      \        "default":"true",
      \			"configuration": {
      \				"request": "launch",
      \				"program": "${workspaceRoot}/main.py",
      \           "stopOnEntry":"true",
      \           "cwd":"${workspaceRoot}"
      \         }
      \	}
		\}
=======
let $generate="cmake -DCMAKE_BUILD_TYPE=Release-DCMAKE_C_COMPILER=/usr/bin/clang-12 -DCMAKE_CXX_COMPILER=/usr/bin/clang++-12 -S /home/zero/cxx/grid/-B /home/zero/cxx/grid-linux/
let $clear="rm -r /home/zero/cxx/grid-linux/"
>>>>>>> e1da866 (1. Изменил .vimrc (попробовать))
