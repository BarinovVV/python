rate_list = [29, 17, 8, 8, 7, 5]
user_rate = int(input("Введите целое число рейтинг "))

if user_rate in rate_list:
    rate_list.insert(rate_list.index(user_rate) + rate_list.count(user_rate), user_rate)
    print(f"Вы стали {rate_list.count(user_rate)}-м с таким же рейтингом")
else:
    for rate in rate_list:
        if rate < user_rate:
            rate_list.insert(rate_list.index(rate), user_rate)
            print(f"Вы заняли {rate_list.index(rate)}-е место в рейтинге")
            break
if rate_list[len(rate_list) - 1] > user_rate:
    rate_list.append(user_rate)
    print(f"Вы заняли крайнее {rate_list.index(user_rate) + 1}-е место в рейтинге")
print(rate_list)