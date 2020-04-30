my_dict = dict()
with open('lesson5_6.txt', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        splitted_line = line.split()
        subject = splitted_line[0]
        sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
        my_dict[subject] = sum_lessons
print(my_dict)
