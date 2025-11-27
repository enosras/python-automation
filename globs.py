import glob



glob_pytool = glob.glob('*.py')
glob_txttool = glob.glob('*.txt')

#flot = glob.glob.__doc__
#print(flot)

''' for item in range(len(glob_pytool)):
    print(len(glob_pytool))
    print(f'Python file found: , {glob_pytool}\n')
'''
print("Python files total:" , len(glob_pytool))
for element in range(len(glob_pytool)):
    #print(len(glob_pytool))
    print(f'File found:  {glob_pytool[element]}')

#if len(glob_pytool) > len(glob_txttool):
    #print("Fewer .py filems than .txt files")
    #print(glob_pytool)
#else:
    #print("Fewer .txt files than .py files")
    #print(glob_txttool)
#print("Done")   









