start_list = [300, 4, 56, 77, 4, 99, 345, 84, 78]

finish_list = [el for i, el in enumerate(start_list) if i != 0 and start_list[i] > start_list[i - 1]]

print(f"Исходный список {start_list} ")
print(f"Обработанный список {finish_list} ")