import subprocess
from subprocess import Popen
import shlex

#help(shlex)
#print(shlex.__doc__)
def cmdOne():
    cmd = "tree "
    trigger = shlex.split(cmd)
    subShell1 = Popen(trigger)
    return subShell1

if __name__ == "__main__":
    p = cmdOne()
    #print(p)
