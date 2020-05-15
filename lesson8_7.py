class ComplexNumber:
    def __init__(self, num_comp):
        self.num_comp = num_comp

    def __str__(self):
        return f'{self.num_comp}'

    def __add__(self, other):
        return f"Сумма комплексных чисел {self.num_comp + other.num_comp}"

    def __mul__(self, other):
        return f"Произвдение комплексных чисел {self.num_comp * other.num_comp}"


cn_1 = ComplexNumber(1 - 2j)
cn_2 = ComplexNumber(3 + 4j)
print(cn_1 + cn_2)
print(cn_1 * cn_2)
