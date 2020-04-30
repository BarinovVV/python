with open('lesson5_5.txt', 'w', encoding="utf-8") as f:
    nums = input('Введите целые числа через пробел: ')
    f.write('Введенные числа: ' + nums + '\n')
    nums = map(int, nums.split())
    sum_nums = sum(nums)
    f.write(f'Сумма чисел: {str(sum_nums)}')
    print(f'Сумма введенных чисел: {sum_nums}')
print('Все записано в файл')
