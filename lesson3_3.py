def my_func(*args):
    return sum(args) - min(args)


print(my_func(11, 25, 31))