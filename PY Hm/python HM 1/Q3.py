# python的整数是任意精度的，不会像C/C++/Java存在溢出的问题(只要内存足够)。
# 使用for循环对[50,123,456]的所有数字进行求和。

Sum = 0
x = 50
while x < 123456:
    Sum = Sum + x
    x = x + 1

print(Sum)
