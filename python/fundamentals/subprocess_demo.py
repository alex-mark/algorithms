import subprocess


# subprocess.run("ls")
# subprocess.run("ls -la", shell=True)
# p1 = subprocess.run(["ls", "-la"], capture_output=True, text=True)


# with open("output.txt", "w") as f:
#     p1 = subprocess.run(["ls", "-la"], stdout=f)


# p1 = subprocess.run(["ls", "-la", "dne"], capture_output=True, text=True)
# p1 = subprocess.run(["ls", "-la", "dne"], capture_output=True, text=True, check=True)
# p1 = subprocess.run(["ls", "-la", "dne"], stderr=subprocess.DEVNULL)


p1 = subprocess.run(["cat", "scope.py"], capture_output=True, text=True)

# print(p1.args)
# print(p1.returncode)
# print(p1.stdout)
# print(p1.stderr)


p2 = subprocess.run(
    ["grep", "-n", "test"], capture_output=True, text=True, input=p1.stdout
)

print(p2.stdout)
