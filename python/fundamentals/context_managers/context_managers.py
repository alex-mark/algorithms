# Context managers handle the teardown of resources automatically
# even when errors occur


import os
from contextlib import contextmanager
from typing import Optional


class OpenFile:
    def __init__(self, filename: str, mode: Optional[str]):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)

        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


@contextmanager
def open_file(filename: str, mode: str):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()


# with OpenFile("sample.txt", "w") as f:
#     f.write("Testing")


with open_file("sample.txt", "w") as f:
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit")

print(f.closed)


#### CD Example ######
@contextmanager
def change_dir(destination: str):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


cwd = os.getcwd()
os.chdir("sample-dir-one")
print(os.listdir())
os.chdir(cwd)

with change_dir("sample-dir-two"):
    print(os.listdir())
