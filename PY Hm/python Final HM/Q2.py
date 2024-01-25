def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


num = 0
prime = []
for x in range(50, 1000):
    if isPrime(x):
        num += 1
        prime.append(x)

print(num)
print(prime)
