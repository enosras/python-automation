import fnmatch
import os
import inspect

ins = inspect.getdoc(fnmatch)
print(ins)  
#help(ins)


FILE_PATH = os.path.dirname(__file__)   
print(f"File path: {FILE_PATH}")
'''

files = os.listdir('.')
for file in files:
    if fnmatch.fnmatch(file, '*.py'):
        print(f"Python file found: {file}")
    '''

#files = os.listdir('.')
#for file in files:
traf = fnmatch.translate('*.py')
print(traf)

#help(fnmatch.fnmatch)


result = fnmatch.fnmatch(FILE_PATH, '*.py')
print(f"Python file found: {result}")


