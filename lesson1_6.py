run_first_day = int(input("Введите сколько вы пробежите в первый день в метрах:  "))
goal_run = int(input("Введите какого результата вы планируете достигнут в метрах:  "))
number_day = 1
today_run = run_first_day
print(f"В {number_day}-й день вы пробежали {run_first_day} метров")
print(f"Ваша цель {goal_run} метров")

while True:
    if today_run >= goal_run:
        break
    else:
        today_run = today_run * 1.1
        number_day += 1
        print(f"На {number_day}-й день вы пробежите {round(today_run, 2)} метров")

print(f"Результат будет достигнут на {number_day}-й  день")
