def cycle(x):
    i = 0
    while True:
        yield x[i]
        if (i+1)%3==0:
            i-=2
        else: i+=1
str = 'abc'
g = cycle(str)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
