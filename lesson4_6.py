from itertools import count, cycle, islice

for i in islice(count(int(input("Введите стартовое число ")), 2), 100):
    print(i)

print([el for el in islice(count(int(input("Введите стартовое число ")), 5), 100)])

lang = ["python", "java", "perl", "javascript", "php", "cobol", "ada"]
count = 1
for item in cycle(lang):
    if count > len(lang) * 3:
        break
    print(item)
    count += 1

