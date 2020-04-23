def int_func(word):
    letters = list(word)
    # print(letters)
    for i in range(len(letters)):
        letters[i] = letters[i].lower()
    letters[0] = letters[0].upper()
    return ''.join(letters)


user_str = "capiTaliZe"

print(int_func(user_str))

user_str_long = "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"
user_list = user_str_long.split()
for i in range(len(user_list)):
    user_list[i] = int_func(user_list[i])

print(' '.join(user_list))


