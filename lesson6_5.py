class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка дочернего класса Pen {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка дочернего класса Pencil {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка дочернего класса Handle {self.title}')


Pen('Шариковя ручка').draw()
Pencil('Чертежный карандаш').draw()
Handle('Несмываемый маркер').draw()
