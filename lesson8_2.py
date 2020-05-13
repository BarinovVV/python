class MyDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(var_1, var_2):
    try:
        var_1, var_2 = int(var_1), int(var_2)
        if var_2 == 0:
            raise MyDivisionError("Деление на ноль не возможно!!!")
        return round(var_1 / var_2, 3)
    except ValueError:
        return "Ошибка ввода данных"
    except MyDivisionError as my_text:
        return my_text


print(div(input("Введите делимое - "), input("Введите делитель - ")))