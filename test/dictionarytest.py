
datas = [{'name': 'jack', 'gender': '男', 'address': '深圳'}, {'name': 'tom', 'gender': '男', 'address': '东莞'},
         {'name': 'jerry', 'gender': '男', 'address': '广州'}, {'name': 'alisi', 'gender': '女', 'address': '深圳'},
         {'name': 'rose', 'gender': '女', 'address': '北京'}, {'name': 'anna', 'gender': '女', 'address': '北京'},
         {'name': 'jack', 'gender': '男', 'address': '深圳'}, {'name': 'tom', 'gender': '男', 'address': '东莞'},
         {'name': 'jerry', 'gender': '女', 'address': '广州'}, {'name': 'alisi', 'gender': '女', 'address': '深圳'},
         {'name': 'rose', 'gender': '男', 'address': '北京'}, {'name': 'anna', 'gender': '女', 'address': '北京'}]

def statistical_data(datas):
    """
    :return: dict
    """
    res_dict = {}
    for data in datas:
        city = data.get('address')
        if city not in res_dict:
            res_dict[city] = 1  # 初始数量1
        else:
            res_dict[city] += 1  # 相同key对应的数量+1
    return res_dict


result = statistical_data(datas)
print(result)
# {'深圳': 4, '东莞': 2, '广州': 2, '北京': 4}