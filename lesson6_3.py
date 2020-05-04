class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}\nдолжность {self.position}'

    def get_total_income(self):
        return f"Суммарный доход составляет {self._income['wage'] + self._income['bonus']}\n"


worker_1 = Position('Валерий', 'Владимирович', 'Python senior', 120000, 50000)
worker_2 = Position('Иван', 'Иванович', 'JS middle', 80000, 30000)

print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_2.get_full_name())
print(worker_2.get_total_income())
