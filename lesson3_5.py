def sum_numbers(num_string):
    num_list = num_string.split()
    result = 0
    for i in range(len(num_list)):
        if num_list[i] != "q":
            result += float(num_list[i])
        else:
            return result
    return result


user_result = 0

while True:
    user_numbers = input("Введите числа через пробел ")
    if 'q' in user_numbers:
        user_result += sum_numbers(user_numbers)
        break
    else:
        user_result += sum_numbers(user_numbers)
        print(f"Сумма введенных числе равна {user_result}")
        print("Продолжайте ввод чисел через пробел для остановки введите в любом месте q")

print(f"Итоговая сумма введенных числе равна {user_result}")







