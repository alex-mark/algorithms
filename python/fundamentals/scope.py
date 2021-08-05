# LEGB
# Local, Enclosing, Global, Built-in


x = "global x"


def test(z):
    # to use global x variable
    # global x
    x = "local x"
    print(x)
    print(z)


test("local z")
print(x)


# do not modify builtins
min = max
m = min([5, 1, 4, 2, 3])
print(m)


def outer():
    x = "outer x"

    def inner():
        # nonlocal x
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()
