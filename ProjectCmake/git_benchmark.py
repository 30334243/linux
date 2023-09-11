import os
import subprocess

def Benchmark():
    subprocess.call(["git","clone","https://github.com/google/benchmark.git"])
    os.chdir("benchmark")
    subprocess.call(["cmake","-E","make_directory","build"])
    subprocess.call(["cmake","-E","chdir","build","cmake","-DBENCHMARK_ENABLE_GTEST_TESTS=OFF","-DCMAKE_BUILD_TYPE=Release","../"])
    subprocess.call(["cmake","--build","build","--config","Release"])
    os.chdir("..")
