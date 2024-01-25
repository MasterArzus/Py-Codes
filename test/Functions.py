# 函数中的形参和实参

def add(a, b=0):
    print("a=", a)
    print("b=", b)
    result = a + b
    return result


c = add(3, 1)  # 必要参数
A = add(b=3, a=1)  # 关键字参数
c = add(1)  # 默认值参数
print(c)


def print_userinfo(name, gender, age, depart):
    print("我是：" + name)
    print("我是 " + gender + "生")
    print("我今年" + str(age) + "岁")
    print("我在" + depart + "工作")


# 默认值参数和调用参数可以改变之前的关键字参数
print_userinfo('小华', '男', 23, '长春')  # 必要参数
print_userinfo('小华')
print("=" * 10)
print_userinfo('小华', age=30, depart='欧亚')


# 可变参数 一个*表示是一个序列类型的可变参数
# **代表是一个字典类型的可变参数
def test(*value):
    print(type(value))  # 证明是序列类型
    for v in value:
        print(v)


# 可变参数调用参数的方式，不可以用元组和序列调用
test('hello', 'world', 'python')


def print_food(*food, placeno, waiter):
    print("这是" + placeno + "菜单")
    for f in food:
        print(f)
    print("服务员：" + waiter)


print_food('宫保鸡丁', '水煮肉片', placeno='12', waiter="小王")
print("a" + "b")
print('a' + 'b')
print('a', 'b', sep='|')
print('a', 'b', sep='|', end='')
# 变量的作用域
a = 'abc'  # 全局变量


def test():
    global a  # 通过函数内部的值改变全局变量
    a = 'def'  # 局部变量
    print(a)


print('调用前的a:', a)
test()
print('调用后的a:', a)

