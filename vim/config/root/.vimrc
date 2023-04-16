"PLUGINS
call plug#begin()
   Plug 'Valloric/YouCompleteMe'
   Plug 'bfrg/vim-cpp-modern'
   Plug 'tpope/vim-commentary'
   Plug 'tpope/vim-surround'
   Plug 'tpope/vim-unimpaired'
   Plug 'tpope/vim-repeat'
   Plug 'fedorenchik/qt-support.vim'
   Plug 'rhysd/clever-f.vim'
   Plug 'Yggdroot/indentLine'
   Plug 'richq/vim-cmake-completion'
   Plug 'tpope/vim-rails'
   Plug 'puremourning/vimspector'
   Plug 'fedorenchik/VimCalc3'
   Plug 'glts/vim-radical'
   Plug 'glts/vim-magnum'
	Plug 'vim-airline/vim-airline'
   " THEMES
   Plug 'morhetz/gruvbox'
call plug#end()
"VIM-AIRLINE
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#formatter = 'jsformatter'
"INDENTLINE
let g:indentLine_concealcursor = 'inc'
let g:indentLine_conceallevel = 2
"YOUCOMPLETEME
let g:ycm_enable_inlay_hints=0
let g:ycm_clear_inlay_hints_in_insert_mode=1
let g:ycm_seed_identifiers_with_syntax=1
let g:ycm_confirm_extra_conf=0
let g:ycm_collect_identifiers_from_tag_files = 1
let g:ycm_clangd_args=['--header-insertion=never']
set completeopt=longest,menu
"VIM-CPP-MODERN
let g:cpp_simple_highlight = 1
let g:cpp_member_highlight = 1
let g:cpp_attributes_highlight = 1
let g:cpp_function_highlight = 1
"NETRW
let g:netrw_banner=0        " disable annoying banner
let g:netrw_liststyle=3     " tree view
"ERRORFORMAT
set errorformat=%E%f:%l:%c:\ %trror:\ %m,%-C,%-Z%p^
set errorformat+=%E%f:%l:%c:\ %tarning:\ %m,%-C,%-Z%p^
set errorformat+=%D%*\\a:\ Entering\ directory\ [`']%f'
set errorformat+=%X%*\\a:\ Leaving\ directory\ [`']%f'
set errorformat+=%-G%.%#
"SETTINGS
autocmd FileType cpp,hpp,h setlocal cindent cino=j1,(0,ws,Ws
autocmd FileType cpp,hpp,h,json setlocal foldlevel=9999
syntax on
filetype plugin indent on
set sessionoptions-=options
set nocp
set noswapfile
set colorcolumn=80
set relativenumber
set number
set expandtab!
set tabstop=3
set shiftwidth=3
set noshowmode
set incsearch
set wildmenu
set wildmode=longest:full,full
set wildoptions=pum
set autowrite
set ignorecase
set smartcase
set cindent
set smartindent
set ttimeoutlen=10
set foldmethod=syntax
set cursorline
set autoindent
set nowrap
" set keymap=russian-jcukenwin
" set statusline=%<%f%h%m%r%=format=%{&fileformat}\ file=%{&fileencoding}\ enc=%{&encoding}\ %b\ 0x%B\ %l,%c%V\ %P
colorscheme desert
"HOTKEY
   let mapleader = " "
	"VIMGREP
	noremap <silent> <leader>f :vimgrep /<C-r>//g **<cr> \| !:copen<cr>
	noremap <silent> <leader>todo :vimgrep /todo/g **<cr> \| !:copen<cr>
   "YOUCOMPLETEME
      nnoremap <silent> <leader>h <Plug>(YCMToggleInlayHints)
      noremap <leader>g :YcmCompleter GoTo<cr>
      noremap <leader>r :YcmCompleter GoToReferences<cr>
      noremap <leader>i <plug>(YCMHover)
   "QUICKFIX
		"FUNCTIONS
		function! ToggleQuickFix()
			if empty(filter(getwininfo(), 'v:val.quickfix'))
				copen
			else
				cclose
			endif
		endfunction
		"HOTKEYS
      noremap <leader>o :call ToggleQuickFix()<cr>
      noremap <leader>n :cnext<cr>
      noremap <leader>p :cprev<cr>
   "USER
      "EXPLORER
         noremap <silent> <leader>e :Explore<cr>
      "WINDOW
         "FOLDING
         map + zo
         map - zc
         "MOVEMENT
            tnoremap <left> <c-w>h
            tnoremap <right> <c-w>l
            noremap <left> <c-w>h
            noremap <down> <c-w>j
            noremap <up> <c-w>k
            noremap <right> <c-w>l
         "CREATE
            noremap ,H :topleft  vnew<cr>
            noremap ,J :botright new<cr>
            noremap ,K :topleft  new<cr>
            noremap ,L :botright vnew<cr>
         "SIZE
            noremap <c-h>    <C-w><
            noremap <c-j>    <C-w>-
            noremap <c-k>    <C-w>+
            noremap <c-l>    <C-w>>
      "BUFFER
         "CREATE
            noremap ,h :leftabove   vnew<cr>
            noremap ,j :rightbelow  new<cr>
            noremap ,k :leftabove   new<cr>
            noremap ,l :rightbelow  vnew<cr>
         "MOVEMENT
            noremap gb :bn<cr>
            noremap gn :bp<cr>
         "CLOSE
            noremap <leader>c :q<cr>
      "REDROW
         noremap ,rr :redraw!<cr>
      "TAB
         noremap ,,h :tabn 1<cr>
         noremap ,,j :tabn 2<cr>
         noremap ,,k :tabn 3<cr>
         noremap ,,l :tabn 4<cr>
