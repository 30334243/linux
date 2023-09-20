import os
import subprocess

def Benchmark():
    subprocess.call(["git","clone","https://github.com/google/benchmark.git"])
    os.chdir("benchmark")
    subprocess.call(["cmake","-E","make_directory","build"])
    subprocess.call(["cmake","-E","chdir","build","cmake","-DBENCHMARK_ENABLE_GTEST_TESTS=OFF","-DCMAKE_BUILD_TYPE=Release","../"])
    subprocess.call(["cmake","--build","build","--config","Release"])
    os.chdir("..")
def CmakeBuild(url):
    subprocess.call(["git","clone",url])
    name = str(url[url.rfind("/")+1:url.__len__()-4])
    os.chdir(name)
    os.mkdir("build")
    os.chdir("build")
    subprocess.call(["cmake",".."])
    subprocess.call(["cmake","--build","."])
    os.chdir("..")
    os.chdir("..")
def SFML(env):
    os.chdir(env)
    if os.path.exists("SFML"):pass
    else:
        os.mkdir("SFML")
    # subprocess.call(["export",'SFML_INSTALL_DIR=${PWD}/SFML'])
    os.system("export SFML_INSTALL_DIR=${PWD}/SFML")
    return
    if os.path.exists("tmp"): pass
    else:
        os.mkdir("tmp")
    os.chdir("tmp")
    subprocess.call(["git","clone","https://github.com/SFML/SFML.git"])
    os.chdir("SFML")
    # debug
    if os.path.exists("build_debug"):pass
    else:
        os.mkdir("build_debug")
    os.chdir("build_debug")
    subprocess.call(["cmake",
                     "-G","Unix Makefiles",
                     "-DCMAKE_BUILD_TYPE=Debug",
                     "-DCMAKE_INSTALL_PREFIX:PATH=\"${SFML_INSTALL_DIR}\"",
                     ".."
                     ])
    subprocess.call(["cmake","--build","."])
    subprocess.call(["cmake","--build",".","--target","install"])
    # release
    if os.path.exists("build_release"):pass
    else :
        os.mkdir("../build_release")
    os.chdir("../build_release")
    subprocess.call(["cmake",
                     "-G","Unix Makefiles",
                     "-DCMAKE_BUILD_TYPE=Release",
                     "-DCMAKE_INSTALL_PREFIX:PATH=\"${SFML_INSTALL_DIR}\"",
                     ".."
                     ])
    subprocess.call(["cmake","--build","."])
    subprocess.call(["cmake","--build",".","--target","install"])
