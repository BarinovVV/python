class Warehouse:
    ''' Склад '''
    __equipments = dict()
    __issued_equipments = dict()

    def add_Equipment(self, key, value):
        ''' Приём '''
        if self.__equipments.get(key) == None:
            self.__equipments[key] = 0
        self.__equipments[key] += value

    def issue_Equipment(self, key, value):
        ''' Выдача '''
        rest = self.__equipments.get(key)
        if rest != None and rest >= value:
            self.__equipments[key] -= value
            if self.__equipments[key] == 0:
                del self.__equipments[key]

    def num(self, key):
        value = self.__equipments.get(key)
        return value if value != None else 0

    def equipments_in_warehouse(self):
        ''' Техника на складе '''
        for i in self.__equipments:
            print(f'{models[i].model} - {self.num(i)} шт.')

    def issued_equipments(self):
        ''' Выданная техника '''
        print(f'\nВыдано в офис:\n{self.__equipments}')

class OfficeEquipment:
    ''' Оргтехника '''

    def __init__(self, model, price, dpi, paper_size):
        self._model = model
        self._price = price
        self._dpi = dpi
        self._paper_size = paper_size

    @property
    def model(self):
        return self._model


class Printer(OfficeEquipment):
    ''' Принтер '''

    def __init__(self, model, price, dpi, paper_size, jet_type):
        self.jet_type = jet_type
        super().__init__(model, price, dpi, paper_size)


class Scanner(OfficeEquipment):
    ''' Сканер '''


class Copier(OfficeEquipment):
    ''' Ксерокс '''

    def __init__(self, model, price, dpi, paper_size, print_speed, monthly_print_volume):
        self.print_speed = print_speed
        self.monthly_print_volume = monthly_print_volume
        super().__init__(model, price, dpi, paper_size)

models = [Printer('HP Color LaserJet Pro M255nw', 19490, '600x600', 'A4', 'laserjet'),
          Printer('Canon PIXMA G1411', 7990, '4800x1200', 'A4', 'inkjet'),
          Copier('Canon i-SENSYS MF744Cdw', 32390, '600x600', 'A3', 27, 10000),
          Copier('МФУ Brother DCP-1602R', 32390, '600x2400', 'A3', 20, 5000),
          Scanner('Canon CanoScan LiDE400', 6290, '4800×4800', 'A4'),
          Scanner('Epson FastFoto FF-680W', 45990, '600×600', 'A5')]

warehouse = Warehouse()
warehouse.equipments_in_warehouse()

while True:
    print('\nВведите тип операции:\n<1> Принять на склад.\n<2> Выдать со склада.\n<Enter> Выход.')
    action = input('> ')
    if action in ['1', '2']:
        s = ''
        for i, eq in enumerate(models):
            s += f'\n<{i}> {eq.model} ({warehouse.num(i)} шт.)'
        while True:
            print(f'\nВведите модель оргтехники и кол-во:{s}')
            try:
                model = int(input('модель > '))
                if model in range(len(models)):
                    n = int(input('кол-во > '))
                    if (n <= 0):
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(f'Некорректный ввод. Введите число от <0> до <{len(models)}>.')
                continue
            else:
                print('\nОперация:')
                if (action == '1'):
                    print(f'Принято на склад {models[model].model} - {n} шт.')
                    print('Текущие остатки на складе:')
                    warehouse.add_Equipment(model, n)
                elif (action == '2'):
                    max = warehouse.num(model)
                    if (n > max):
                        n = max
                        print(f'Внимание: На складе всего {n} шт. {models[model].model}!')
                    print(f'Выдано со склада {models[model].model} - {n} шт.')
                    print('Текущие остатки на складе:')
                    warehouse.issue_Equipment(model, n)

                warehouse.equipments_in_warehouse()
                break

    elif action == '':
        break
    else:
        print('Некорректный ввод. Для выбора введите <1> или <2>.')

print(f'Осталось на складе: {}')
warehouse.equipments_in_warehouse()
