class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}!')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} - {self.speed}! Вы превышаете скорость!')
        else:
            print(f'Скорость автомобиля {self.name} - {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} - {self.speed}! Вы превышаете скорость!')
        else:
            print(f'Скорость автомобиля {self.name} - {self.speed}')


class PoliceCar(Car):
    pass


my_car = SportCar(150, 'red', 'Ferrari', False)
town_car = TownCar(70, 'black', 'Mercedes', True)
police_car = PoliceCar(150, 'yellow', 'Ford', False)
work_car = WorkCar(40, 'green', 'Volvo', False)

my_car.go()
my_car.stop()
my_car.turn('лево')
my_car.show_speed()
town_car.show_speed()
police_car.show_speed()
work_car.show_speed()