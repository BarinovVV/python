with open('lesson5_3.txt', encoding="utf-8") as f:
    salaries = []
    lines = f.readlines()
    for line in lines:
        name, salary = line.split(' - ')
        salaries.append(int(salary))
        if int(salary) < 20000:
            print(line, end='')
    print(f'\nСредняя зп: {round((sum(salaries) / len(salaries)), 2)}')