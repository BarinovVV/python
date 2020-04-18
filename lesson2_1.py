my_list = [False, None, ZeroDivisionError, complex(5, 6), b'text00', bytearray(b"some text"), {1, 'a', 5.6}, 1, 1.25, 'string', [1, 2, 3], ('a', 123, [5, 6.5]), {'name': 'Valery', "age": 50}]
for el in my_list:
    print(type(el))
