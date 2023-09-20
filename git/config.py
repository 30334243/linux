import os

home=os.getenv("HOME")
os.chdir(home)
git_config=open(".gitconfig","a+")
git_config.write("[color]\n"
                 "\tui = true\n")
git_config.write("[alias]\n"
                 "\ts = status\n"
                 "\tl = log --graph --oneline\n")
