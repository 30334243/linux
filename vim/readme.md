# VIM
## Plugins
### 1. Markdown
#### 1. Livedown
1.1 Установить "Nodejs"
~~~
sudo apt install npm
sudo npm install -g livedown
~~~
1.2 Добабить в **.vimrc** плагин и hotkey для включения или отключения плагина
~~~
"плагин
Plug 'shime/vim-livedown'
"hotkey
nnoremap ,md : LivedownToggle<cr>
~~~
#### 2. Markdown-preview
1.1 Добабить в **.vimrc** плагин и hotkey для включения или отключения плагина
~~~
"плагин
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}
"hotkey
nmap ,md <Plug>MarkdownPreviewToggle
~~~
