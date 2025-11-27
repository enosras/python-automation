import fnmatch
import os


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
result = fnmatch.fnmatch(FILE_PATH, '*.py')
print(f"Python file found: {result}")


