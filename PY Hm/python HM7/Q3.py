import pandas as pd

ser = pd.Series(['fInD', 'yoUR', 'KNEE'])
i = 0
for word in ser:
    Up1 = word[0].isupper()
    if not Up1:
        Capital = word[0].upper()
        word = word.replace(word[0], Capital)
    Low2 = word[1].islower()
    if not Low2:
        Low = word[1].lower()
        word = word.replace(word[1], Low)
    ser[i] = word
    i += 1
print(ser)
