
def valid_number():
    numbers = []

    for x in range(1, 6):
        for y in range(0, 6):
            for a in range(0, 6):
                for b in range(0, 6):
                    for c in range(0, 6):
                        numbers += [10000*x + y*1000 + a*100 + b*10 + c]
    print(numbers)

    return len(numbers)


print(valid_number())
