# static or classless
# """
# os.path 
# old style
# """
# Class based 
# path from pathlib library
#     python 3.6 or higher
from pathlib import Path
cwd = Path.cwd()

#Combine parts to create full path and file name 
new_file = Path.joinpath(cwd, 'new_file.txt')
print(new_file)

# get the parent directory
parent = cwd.parent
 #Does this exist?
# print(str(new_file.exists()))
# checking for directory or file
print(parent.is_file())
print(parent.is_dir())
# List child directories
for child in parent.iterdir():
    if child.is_dir():
        print(child)
