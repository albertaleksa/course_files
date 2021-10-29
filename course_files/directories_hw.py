import os

cur_dir = os.getcwd()
len_cur_path = len(cur_dir.split('/'))

# print(os.getcwd())
main = "main_folder"
main_path = os.path.join(cur_dir, main)


def create_dir_files():
    os.mkdir(main_path)
    file = os.path.join(main_path, "main_file1.txt")
    open(file, mode='a').close()

    sub_path1 = os.path.join(main_path, "sub_folder1")
    os.mkdir(sub_path1)
    file = os.path.join(sub_path1, "sub_file1.txt")
    open(file, mode='a').close()
    file = os.path.join(sub_path1, "sub_file2.txt")
    open(file, mode='a').close()
    file = os.path.join(sub_path1, "sub_file3.txt")
    open(file, mode='a').close()

    sub_path2 = os.path.join(main_path, "sub_folder2")
    os.mkdir(sub_path2)
    file = os.path.join(sub_path2, "sub_file1.jpg")
    open(file, mode='a').close()
    file = os.path.join(sub_path2, "sub_file2.jpg")
    open(file, mode='a').close()
    file = os.path.join(sub_path2, "sub_file3.jpg")
    open(file, mode='a').close()

    sub_sub_path1 = os.path.join(sub_path1, "sub_sub_folder1")
    os.mkdir(sub_sub_path1)
    file = os.path.join(sub_sub_path1, "sub_file1")
    open(file, mode='a').close()
    file = os.path.join(sub_sub_path1, "sub_file2")
    open(file, mode='a').close()
    file = os.path.join(sub_sub_path1, "sub_file3")
    open(file, mode='a').close()


def read_dir(folder):
    for root, dirs, files in sorted(os.walk(folder)):
        path = root.split(os.sep)
        dif_path = len(path) - len_cur_path
        print((dif_path - 2) * '|   ', '.' if dif_path < 2 else '|---', '[', os.path.basename(root), ']', sep="")
        for f in files:
            print((dif_path-1) * '|   ', '|---', f, sep="")


read_dir(main_path)
