from sys import argv

script_name, product_hours, rate_hour, percent_award = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", product_hours)
print("Ставка в час: ", rate_hour)
print("Процент премии: ", percent_award)

print(f"Заработная плата сотрудника = {(float(product_hours) * float(rate_hour)) * ((100 + float(percent_award)) / 100)}")
