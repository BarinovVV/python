from functools import reduce

print(reduce(lambda x, y: x * y, [el for el in range(100, 201) if el % 2 == 0]))