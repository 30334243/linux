import os
import subprocess
from subprocess import Popen

def FindDefaultCompiler(compiler):
    compiler_ver_default = ""
    for filename in os.listdir("/usr/bin"):
        if filename.startswith(compiler) and len(filename)==len(compiler):
            p = Popen([compiler,"-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            errors, output = p.communicate()
            find_compiler_ver = compiler+" version "
            beg = output.find(find_compiler_ver)+len(find_compiler_ver)
            end = 0
            if compiler == "clang":
                end = output.find("\n",beg)
            elif compiler == "gcc":
                end = output.find(" ",beg)
            compiler_ver_default = str(output[beg:end])
    return compiler_ver_default

def ListOfCompilers(compiler):
    compiler_ver_default = FindDefaultCompiler(compiler)
    for filename in os.listdir("/usr/bin"):
        if filename.startswith(compiler) and not len(filename)==len(compiler):
            beg = len(compiler)+1
            msg_tail = filename[beg:len(filename)]
            if msg_tail.isdecimal():
                if compiler_ver_default.startswith(msg_tail):
                    print(compiler+"-"+filename[beg:len(filename)]+" (Версия по умолчанию: "+compiler_ver_default+")")
                    return 1
                else:
                    print(compiler+"-"+filename[beg:len(filename)])
                    return 1

def ListOfFindCompilers(func,*compilers):
    for compiler in compilers:
        func(compiler)


a=["gcc","clnag"]
f=ListOfCompilers
map(f,a)
