import os

my_file = "file.txt"

# change dir to the directory when stored program-file "files.py"
# will work from every place
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# os.path.abspath(my_file)

"""
open()
mode=
    r  - read (default)  Pointer - Beginning of file. FileNotFoundError - if file doesn't exist
    r+ - read & write    Pointer - Beginning of file. FileNotFoundError - if file doesn't exist
    w  - write           Pointer - Beginning of file. Will create - if file doesn't exist. If exists - will rewrite
    w+ - read & write    Pointer - Beginning of file. Will create - if file doesn't exist. If exists - will rewrite
    a  - write           Pointer - End of file.       Will create - if file doesn't exist. File will not rewrite
    a+ - read & write    Pointer - End of file.       Will create - if file doesn't exist. File will not rewrite
    x  - create file for writing.                     FileExistsError - if file doesn't exist
    x+ - create file for read & writing.              FileExistsError - if file doesn't exist
    
modificator=
    b - binary
    t - text (default)
    
"""
# Open/create file for write and write info
f = open(my_file, "w", encoding="utf-8")
f.write("String1\nString2\n")
f.close()

# Open file for read and read info
f = open(my_file, "r", encoding="utf-8")
# 1 method
# for line in f:
#     print(line, end='')
# 2 method
text = f.read()
f.close()
print(text)

# Open/create file for update and add info
lines = ["String3", "String4"]
f = open(my_file, "a", encoding="utf-8")
# 1 method
# for i in lines:
#     f.write(i + '\n')
# 2 method
f.writelines(f"{i}\n" for i in lines)
f.close()

# file closes implicitly
with open(my_file, "r", encoding="utf-8") as f:
    for line in f:
        print(line, end='')
