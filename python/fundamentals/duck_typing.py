# Duck typing and Easier to ask forgiveness than permission (EAFP)

import os


class Duck:
    def quack(self):
        print("Quack, quack")

    def fly(self):
        print("Flap, flap")


class Person:
    def quack(self):
        print("I'm quacking like a duck")

    def fly(self):
        print("I'm flapping my arms")


def quack_and_fly(thing):
    # Not Duck-typed (Non-pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print("This has to be a Duck")

    # LBYL: Look Before You Leap (Non-Pythonic)
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # EAFP
    try:
        thing.quack()
        thing.fly()
        # thing.bark()
    except AttributeError as e:
        print(e)

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)


my_list = [1, 2, 3, 4, 5, 6]

# Non-Pythonic
if len(my_list) >= 6:
    print(my_list[5])
else:
    print("That index does not exist")

# Pythonic
try:
    print(my_list[5])
except IndexError:
    print("That index does not exist")


# File example from python docs


my_file = "/tmp/test.txt"

# Race condition
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print("File can not be accessed")

# No Race-condition
try:
    f = open(my_file)
except IOError as e:
    print("File can not be accessed")
else:
    with f:
        print(f.read())
