from time import sleep
from itertools import count


class TrafficLight:
    def __init__(self):
        self.__color = ('красный', 'желтый', 'зеленый')

    def running(self):
        i = int(input('Введите количество циклов светофора - '))
        for el in count():
            if el > i:
                print(f'\033[0mИспытания светофора прошли успешно')
                break
            else:
                print(f'\033[31mСТОЯТЬ - сейчас 7 секунд будет гореть {self.__color[0]} свет')
                sleep(7)
                print(f'\033[33mПРИГОТОВИТЬСЯ - теперь 2 секунды горит {self.__color[1]} свет')
                sleep(2)
                print(f'\033[32mМОЖНО ЕХАТЬ - 30 секунд горит {self.__color[2]} свет')
                sleep(10)


test_light = TrafficLight()

test_light.running()

# print(light._TrafficLight__color)
