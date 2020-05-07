class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f'Сумма ячеек - {str(self.nums + other.nums)}'

    def __sub__(self, other):
        return f'Разность ячеек - {self.nums - other.nums}' if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше или равно второй, вычитание невозможно'

    def __mul__(self, other):
        return f'Произведение ячеек - {str(self.nums * other.nums)}'

    def __truediv__(self, other):
        return f'Частное ячеек - {self.nums // other.nums}'


cell_1 = Cell(225)
cell_2 = Cell(102)
cell_3 = Cell(336)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 - cell_3)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(48))