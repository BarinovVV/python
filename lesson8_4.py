class Warehouse:
    ''' Склад '''
    __equipments = dict()
    __issued_equipments = dict()


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
