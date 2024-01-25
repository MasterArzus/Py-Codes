from collections import Counter


def count_letter():
    with open('Q2.txt', 'r') as f:
        text = f.read()
        text = text.lower()
    # 这一步为读取文件

    c = Counter()
    # 这一步为制造一个counter

    for word in text:
        c[word] = c[word] + 1
    # 这一步为数word中的各个单词的数

    return c


print(count_letter())
