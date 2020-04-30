with open('lesson5_2.txt') as f:
    lines = f.readlines()
    print('Количество строк:', len(lines))
    for num_line, line in enumerate(lines, start=1):
        print(f'{num_line} строка содержит - {len(line.split())} слов')