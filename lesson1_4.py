user_number = int(input("Введите число  "))
max_number = 0

while user_number >= 10:
    if user_number % 10 > max_number:
        max_number = user_number % 10
    user_number = user_number // 10
    print(user_number)
if user_number > max_number:
    max_number = user_number

print(max_number)