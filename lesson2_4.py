user_string = 'приведено описание ключевых встроенных типов данных реализованных в Python'
user_list = user_string.split()
print(user_list)
for word in range(len(user_list)):
    print(f"{word + 1} {user_list[word][:10]}")