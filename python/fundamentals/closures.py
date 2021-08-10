def outer_func(msg: str):
    message = msg

    def inner_func():
        # message is a free variable (it is not a function argument)
        print(message)

    return inner_func


# Closure closes over the free variables from their enviroment
hi_func = outer_func("hi")
hello_func = outer_func("hello")

print(hi_func.__name__)
hi_func()
hello_func()
