# реализация програмного заполнения структуры с запросом данных по товарам у пользователя
goods_list = []
i = 0
while True:
    goods_list.append((i + 1, {}))
    goods_list[i][1]['название'] = input("Название ")
    goods_list[i][1]['цена'] = int(input("Цена "))
    goods_list[i][1]['количество'] = int(input("Количество "))
    goods_list[i][1]['ед'] = input("Единица измерения ")
    i += 1
    user_desire = input('Продолжим ввод товаров y/n')
    if user_desire.upper() != 'Y':
        break

print(goods_list)

# реализация аналитики о товарах в каталоге
goods_list_analitic = [
    (1, {'название': 'макак', 'цена': 1, 'количество': 1, 'ед': 'как'}),
    (2, {'название': 'rgrg', 'цена': 45, 'количество': 3, 'ед': 'gny'}),
    (3, {'название': 'пекркпк', 'цена': 4434, 'количество': 32, 'ед': 'tпкпк'}),
    (4, {'название': 'щлоннлнли', 'цена': 445, 'количество': 4, 'ед': 'tргйл'}),
    (5, {'название': 'гйгйривио', 'цена': 99238, 'количество': 324, 'ед': 'оыйшы'}),
]

analytic_dict = {}
for key in goods_list[0][1]:
    analytic_dict[key] = []
    for i in range(len(goods_list_analitic)):
        analytic_dict[key].append(goods_list_analitic[i][1][key])

print(analytic_dict)