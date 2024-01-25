import numpy as np

seed1 = int(input("输入学号后五位:\n"))
np.random.seed(seed1)
a = np.random.randint(2, 11, (5, 5))

print('原始数组：')
print(a)

print('交换2、3行的数组：')
a[[1, 2]] = a[[2, 1]]
print(a)

print('交换1、5列的数组：')
a[:, [0, 4]] = a[:, [4, 0]]
print(a)

print('均值:')
print(np.mean(a))
print('方差:')
print(a.var())