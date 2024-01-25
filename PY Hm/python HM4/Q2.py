import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print("运行时间为：" + str(stop - start))
    return wrapper


# 使用样例：
@timeit
def func(num):
    return sum(range(num))


timeit(func(1000000))
