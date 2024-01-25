import csv


def mean(datas, word):
    result_dict = {}
    for data in datas:
        place = data.get(word)
        price = int(data.get('人均价格')[1:])
        if place not in result_dict:
            result_dict[place] = [1, price, 0]
        else:
            result_dict[place][0] += 1
            result_dict[place][1] += price

        result_dict[place][2] = round(result_dict[place][1] / result_dict[place][0], 2)

    return result_dict


with open('data.csv', 'r', newline='', encoding='UTF-8') as f:
    reader1 = csv.DictReader(f)

    print(mean(reader1, '餐厅种类'))

with open('data.csv', 'r', newline='', encoding='UTF-8') as f:
    reader1 = csv.DictReader(f)

    print(mean(reader1, '所在地区'))

with open('data.csv', 'r', newline='', encoding='UTF-8') as f:
    reader1 = csv.DictReader(f)

    print(mean(reader1, '评分'))
