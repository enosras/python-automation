import os
import shutil

# sh = shutil
cursor = os.mkdir("new_director")
print(cursor)
d = os.rmdir("new_director")
print("Directory created and removed successfully!", d)


s = shutil.which("ls")
print(s)

a = os.chdir("/Users/enos/pylibs")
print(a)
pwd = os.getcwd()
print(pwd)

a = os.chdir("/Users/enos")
print(a)
pwd = os.getcwd()
print(pwd)
files = os.listdir("/Users/enos/pylibs")
print(files)


os.cpu_count
print(os.cpu_count())
os.name
print(os.name)
print(os.sep)
os.sep
print(os.sep)
os.linesep
print(os.linesep)
os.pathsep
print(os.pathsep)

k = os.__doc__
print(k)
