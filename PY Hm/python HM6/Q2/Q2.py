import csv
import json


def counter(datas, word):
    result_dict = {}
    for data in datas:
        key = data.get(word)
        if key not in result_dict:
            result_dict[key] = 1
        else:
            result_dict[key] += 1

    return result_dict


ipdic = {}

with open('weblog.csv', 'r', newline='', encoding='UTF-8') as f:
    reader1 = csv.DictReader(f)
    ipdic = counter(reader1, 'IP')
    for item in range(4):
        ipdic.popitem()

    print(ipdic)
    json_data = json.dumps(ipdic)
    with open("ip frequncy.json", "w") as f_six:
        f_six.write(json_data)
