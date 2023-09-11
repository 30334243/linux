import os
import sys
import MyColor as Color
import MyCmake as CMake

# 1. name-project
# .  project-path
# .  environment-path
# .  cmake-version
# .  qt
# .  gprof
# .  googletest
# .  benchmark
print(Color.GREEN+"Example:")
print(Color.PURPLE+"  1. python "+Color.GREEN +"MyCreateProject.py "+
      Color.YELLOW+"Project"+Color.END)
args = sys.argv
if args.__len__() <= 1:
    print(RED+"Не достаточно аргументов"+END)
    exit()
project_name = args[1]
project_path = ""
environment_path = ""
for arg in args:
    if arg.startswith("project-path="):
        project_path = str(arg[13:])
    if arg.startswith("environment-path="):
        environment_path = str(arg[17:])
if project_path == "" and (not os.path.exists(project_name)):
    os.mkdir(project_name)
    os.chdir(project_name)
elif project_path == "" and os.path.exists(project_name):
    os.chdir(project_name)
elif project_path != "" and (not os.path.exists(project_path)):
    os.mkdir(project_path)
    os.chdir(project_path)
elif project_path != "" and os.path.exists(project_path):
    os.chdir(project_path)
elif environment_path != "" and (not os.path.exists(environment_path)):
    os.mkdir(environment_path)
else:
    print(Color.RED+"Error!!!"+Color.END)
    exit()
CMake.CreateCMakeLists(project_path,project_name,environment_path,args[1:])
