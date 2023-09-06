import sys
import os

args = sys.argv
name = args[1]
print(name)
file = open(name,"w+")
file.write("#ifndef "+name.upper()+"_HPP\n")
file.write("#define "+name.upper()+"_HPP\n")
file.write("\n#endif\n")
