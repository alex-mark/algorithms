import os
from datetime import datetime

print(os.getcwd())

# os.mkdir('os-test')
os.makedirs("os-demo/sub-dir")  # creates nested folders

# os.rmdir('os-test')
os.removedirs("os-demo/sub-dir")  # removes nested folders

# os.rename("test.txt", "demo.txt")
mod_time = os.stat("sorting.ipynb").st_mtime
print(datetime.fromtimestamp(mod_time))

# traverse path
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print()

# print(os.listdir())

# print(os.environ.get("HOME"))

file_path = os.path.join(os.environ.get("HOME"), "test.txt")
print(file_path)

# (dir, basename)
print(os.path.split("/tmp/test.txt"))

print(os.path.exists("/tmp/test.txt"))
print(os.path.isdir("/tmp/test.txt"))
print(os.path.isfile("/tmp/test.txt"))

# ('/tmp/test', '.txt')
print(os.path.splitext("/tmp/test.txt"))
