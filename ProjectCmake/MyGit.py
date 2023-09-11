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
