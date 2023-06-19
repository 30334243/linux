import os
import subprocess
from  sty import fg,bg,ef,rs

def Empty():None
def SimpleCmake():
    subprocess.run(["cmake",".."])
    subprocess.run(["cmake","--build","."])
def Build(name,repo,func,cmake):
    if os.path.exists(name):
        print('{}"{}" уже существует{}'.format(fg.yellow,name,fg.rs))
        return
    
    cur_dir = os.path.abspath(os.curdir)

    subprocess.run(["git","clone",repo])
    os.chdir(name)

    func()

    if not os.path.exists("build"):
        os.mkdir("build")

    os.chdir("build")

    cmake()

    os.chdir(cur_dir)
