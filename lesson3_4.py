def exponent(x, y):
    result = 1
    if y == 0:
        return 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


print(exponent(9, -4))


def recurcion_exponent(x, y):
    if y > 0:
        return x * recurcion_exponent(x, y-1)
    elif y < 0:
        return 1.0 / recurcion_exponent(x, -y)
    return 1


print(recurcion_exponent(9, -3))