from itertools import count


def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


def factorial_gen():
    for f in count(1):
        yield factorial(f)


i = 1
for el in factorial_gen():
    print(f"Факториал {i} - {el}")
    if i == 15:
        break
    i += 1

