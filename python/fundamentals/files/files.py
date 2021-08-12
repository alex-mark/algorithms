# File objects

# r - read; w - write; a - append; r+ - read & write
# b - for binary files
# f = open("test.txt", "r")
# print(f.mode)
# f.close()

with open("test.txt", "r") as f:
    # f_contents = f.read()
    f_contents = f.readlines()
    print(f_contents)

with open("test.txt", "r") as f:
    f_contents = f.readline()
    print("Reading one line:", f_contents, end="")

    for line in f:
        print(line, end="")


print()
print(f.closed, "\n")

# Read large file in chunks
with open("test.txt", "r") as f:
    size_to_read = 10
    # read n characters of a file
    f_contents = f.read(size_to_read)
    print(f_contents, end="")

    # Current cursor position
    # print(f.tell())

    f.seek(0)  # move cursor
    f_contents = f.read(size_to_read)
    print(f_contents, end="")

    # while len(f_contents) > 0:
    #     print(f_contents, end="*")
    #     f_contents = f.read(size_to_read)


with open("test2.txt", "w") as f:
    f.write("Test")
    f.seek(2)
    f.write("Test")


# Working with two files
# Context manager can open two files but it is less readable
# with open('test.txt', 'r') as rf, open('test_copy.txt', 'w') as wf:
with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)
