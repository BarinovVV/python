def division(a, b):
    return round(a / b, 2)


div_1 = float(input("Ввведите делимое: "))
div_2 = float(input("Ввведите делитель: "))

try:
    print(division(div_1, div_2))
except ZeroDivisionError:
    print("Делить на НОЛЬ нельзя!")


