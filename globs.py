import glob


glob_pytool = glob.glob('*.py')
glob_txttool = glob.glob('*.txt')

if len(glob_pytool) > len(glob_txttool):
    print("Fewer .py files than .txt files")
    print(glob_pytool)
else:
    print("Fewer .txt files than .py files")
    print(glob_txttool)
print("Done")   







