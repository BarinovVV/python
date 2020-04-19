user_list = list(input('Введите слово или любой набор на клавиатуре '))
print(f"Введенный список {user_list}")

for i in range(1, len(user_list), 2):
    temp = user_list[i]
    user_list[i] = user_list[i - 1]
    user_list[i - 1] = temp

print(f"Измененный список {user_list}")
