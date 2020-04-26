start_list = [300, 4, 56, 77, 4, 99, 345, 84, 78]
# finish_list =[]

# for i in range(1, len(start_list)):
#     if start_list[i] > start_list[i-1]:
#         finish_list.append(start_list[i])

finish_list = [el for i, el in enumerate(start_list) if start_list[i] > start_list[i - 1] and i != 0]

print(f"Исходный список {start_list} ")
print(f"Обработанный список {finish_list} ")

