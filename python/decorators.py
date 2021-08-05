from typing import Callable
import logging
import time
from functools import wraps


# closure example
def outer_function(msg: str):
    def inner_function():
        print(msg)

    return inner_function


hi_func = outer_function("Hi")
bye_func = outer_function("Bye")

# hi_func()
# bye_func()


def decorator_function(original_function: Callable):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed:", original_function.__name__)
        return original_function(*args, **kwargs)

    return wrapper_function


class decorator_class(object):
    def __init__(self, original_function: Callable):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method executed:", self.original_function.__name__)
        return self.original_function(*args, **kwargs)


# @decorator is same as my_func = decorator(my_func)
# display = decorator_function(display)
@decorator_function
def display():
    print("display function ran")


# @decorator_function
@decorator_class
def display_info(name: str, age: int):
    print(f"display_info ran with args: {name}, {age}")


# display()
# display_info("John", 25)


#
# Practical example
#
def my_logger(orig_func):
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kwargs: {kwargs}")

        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} seconds")
        return result

    return wrapper


@my_logger
@my_timer
def display_info2(name: str, age: int):
    print(f"display_info2 ran with args: {name}, {age}")


display_info2("Alice", 20)
