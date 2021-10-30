import os
import shutil
import time

# check if file or dir exists
# os.R_OK - check for access for read dir/file
# os.W_OK - check for access for write dir/file
# os.X_OK - check if dir/file executable
print(os.access("file.txt", os.F_OK))

# change access rights for file/dir
# os.chmod("file.txt", 0o777)
# os.chmod("file.txt", 0o644)

# copy without metadata and permissions
shutil.copyfile(r"file.txt", r"file2.txt")
# copy with permissions but without metadata (like the file’s creation and modification times)
shutil.copy(r"file.txt", r"file3.txt")
# copy with metadata and permissions
shutil.copy2(r"file.txt", r"file4.txt")
# move file
shutil.move(r"file4.txt", r"file5.txt")
# rename file
os.rename(r"file5.txt", r"file7.txt")
# remove file
os.remove(r"file7.txt")
# remove file
os.unlink(r"file3.txt")
os.unlink(r"file2.txt")

# check if file exists
print(os.path.exists(r"file.txt"))
# get file's size in bytes
print(os.path.getsize(r"file.txt"))

# get last time of access to file in UNIX time
t = os.path.getatime(r"file.txt")
print(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(t)))
# get time of file's creation in UNIX time
t = os.path.getctime(r"file.txt")
print(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(t)))
# get time of the last file's modification in UNIX time
t = os.path.getmtime(r"file.txt")
print(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(t)))

# os.stat() - get file's metadata
s = os.stat(r"file.txt")
print(s)

# os.path.basename(<path>) - get file name without path
# os.path.dirname(<path>) - get dir path to file
# os.path.split(<path>) - return tuple (<path to dir>, <file name>)
# os.path.join(<path1>, <path2>, .. , <pathN>) - concat paths to one path (add separates if needed)
# os.path.normpath(<path>) - make correct path from incorrect (appropriate separates)
