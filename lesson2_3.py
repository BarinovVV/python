user_number = int(input("Введите целое число от 1 до 12: "))
months = ('январь', 'февраль', 'март', "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
          'декабрь')
if 1 <= user_number <= 2 or user_number == 12:
    print(f"Вы ввели месяц {months[user_number - 1].upper()} это ЗИМА")
elif 3 <= user_number <= 5:
    print(f"Вы ввели месяц {months[user_number - 1].upper()} это ВЕСНА")
elif 6 <= user_number <= 8:
    print(f"Вы ввели месяц {months[user_number - 1].upper()} это ЛЕТО")
elif 9 <= user_number <= 11:
    print(f"Вы ввели месяц {months[user_number - 1].upper()} это ОСЕНЬ")