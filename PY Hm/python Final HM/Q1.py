a = 0
b = 0

for x in range(10, 100001):
    if x % 5 == 0:
        a += x
    if x % 7 == 0:
        b += x

print("The sum of 5s is:")
print(a)
print("The sum of 7s is:")
print(b)
