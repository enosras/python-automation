import shutil
import os

shutil.copy("source.txt","destination.txt")

d = os.getcwd
c = shutil.which("python")
print(c)
print(f"your path is: {d}")
