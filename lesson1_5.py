revenue = float(input("Введите выручку:  "))
cost = float(input("Введите издержки:  "))
is_profit = False
if revenue > cost:
    print(f"Поздравляю - вы работаете с прибылью равной - {round((revenue - cost), 2)}")
    is_profit = True
    print(f"Ваша рентабельность равна {round(((revenue - cost) / revenue * 100), 2)} процентов!")
elif revenue < cost:
    print(f"К сожалению у вас убытки в размере - {round((cost - revenue), 2)}")
else:
    print("Вы сработали безубыточно!")

number_staff = int(input("Введите численность персонала:  "))
if is_profit:
    print(f"Прибыль в расчете на одного сотрудника равна  {round(((revenue - cost) / number_staff), 2)}")


