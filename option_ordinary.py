import csv


def parcer(old_stock, new_stock):
    old_list = []
    new_list = []
    new_vin_list = []
    old_vin_list = []

    with open(old_stock, newline='', encoding='utf-8') as old_stock:
        reader_old = csv.reader(old_stock)
        for row in reader_old:
            old_list.append(row)
            old_vin_list.append(row[0])

    del old_list[0]
    old_list.sort()

    with open(new_stock, newline='', encoding='utf-8') as new_stock:
        reader_new = csv.reader(new_stock)
        for row in reader_new:
            new_list.append(row)
            new_vin_list.append(row[0])

    del new_list[0]
    new_list.sort()

    def difference_price():
        for new_values in new_list:
            if new_values[2] == '':
                new_values[2] = new_values[1]
            for old_values in old_list:
                if new_values[0] == old_values[0]:
                    old_values.append(new_values[1])
                    old_values.append(new_values[2])
                    if old_values[2] == '':
                        old_values[2] = old_values[1]

        for value in old_list:
            if len(value) == 5:

                if value[1] != value[3]:
                    print(f'В модели {value[0]} нужно заменить розничную цену')

                if value[2] != value[4]:
                    print(f'В модели {value[0]} нужно заменить актуальную цену')

        print('')

    def add_del():
        add_vins = list(set(new_vin_list) - set(old_vin_list))
        for vin in add_vins:
            print(f'Нужно добавить - {vin}')

        del_vins = list(set(old_vin_list) - set(new_vin_list))
        for vin in del_vins:
            print(f'Нужно удалить - {vin}')

    difference_price()
    add_del()


print('')
parcer('old.xlsx', 'new.xlsx')