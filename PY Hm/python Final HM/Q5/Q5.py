import csv


def mean(datas, word):
    result_dict = {}
    for data in datas:
        keyword = data.get(word)
        price = int(data.get('人均价格')[1:])
        if keyword not in result_dict:
            result_dict[keyword] = [1, price, 0]
        else:
            result_dict[keyword][0] += 1
            result_dict[keyword][1] += price

        result_dict[keyword][2] = round(result_dict[keyword][1] / result_dict[keyword][0], 2)

    return result_dict


with open('data.csv', 'r', newline='', encoding='UTF-8') as fr:
    reader = csv.DictReader(fr)

    result1 = mean(reader, '评分')

    mean_list = []
    for item in result1:
        mean_list.append([item, result1[item][2]])

    mean_list.sort(key=(lambda x: x[1]))

    print(mean_list)

    fw = open('不同评分的餐厅人均价格平均值.csv', 'w')
    writer = csv.writer(fw)
    writer.writerow(['评分', '人均价格的平均值'])
    for i in mean_list:
        writer.writerow(i)
    fw.close()
fr.close()
