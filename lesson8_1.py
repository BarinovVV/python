class Data:
    def __init__(self, string_data):
        Data.string_data = string_data

    @classmethod
    def extract(cls):
        input_data = list(map(int, cls.string_data.split('-')))
        return input_data

    @staticmethod
    def check_data():
        data_list = Data.extract()
        if (0 < data_list[0] < 31) and (0 < data_list[1] < 13) and (0 < data_list[2] < 1000):
            val = f"Введенная дата {Data.string_data} корректна"
        else:
            val = f"Введенная дата {Data.string_data} не корректна"
        return val


data_1 = Data("12-12-20")
print(data_1.extract())
print(data_1.check_data())

data_2 = Data("13-13-20")
print(data_2.extract())
print(data_2.check_data())