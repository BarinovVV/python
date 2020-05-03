class Road:
    def __init__(self, length, width):
        self._length_road = length
        self._width_road = width
        self.weight_cm_square_metre = 25
        self.height_cm_asphalt = 5

    def total_weight(self):
        return self._length_road * self._width_road * self.weight_cm_square_metre * self.height_cm_asphalt


asphalt = Road(float(input('Введите длину дороги в метрах - ')), float(input('Введите ширину дороги в метрах - ')))

print(f'Общий вес асфальта составит {asphalt.total_weight() / 1000} тонн')
