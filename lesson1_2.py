number_seconds = int(input("Введите количество секунд "))
print(f"Вы ввели {number_seconds}")
user_desire = input("Хотите перевести введеные секунды в часы и минуты? (Y/N)")
if user_desire == 'Y' or user_desire == 'y':
    hours = int(number_seconds / 60 / 60)
    # if hours < 10:
    #     hours = str(0) + str(hours)
    minutes = int(number_seconds / 60 % 60)
    # if minutes < 10:
    #     minutes = str(0) + str(minutes)
    seconds = number_seconds % 60
    # if seconds < 10:
    #     seconds = str(0) + str(seconds)
    print(f"Время  = {hours:02}:{minutes:02}:{seconds:02}")
else:
    print("До свидания!")
