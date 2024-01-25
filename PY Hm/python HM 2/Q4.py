def count_letter():
    with open("Q4.txt", "r") as f:
        text = f.read()

    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~\n \'':
        text = text.replace(ch, "")

    words = text.lower()
    counts = {}
    for i in words:
        counts[i] = counts.get(i, 0) + 1

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)

    for i in range(24):
        character, count = items[i]
        print("{0:<10}{1:>5}".format(character, count))

    return counts


print(count_letter())
