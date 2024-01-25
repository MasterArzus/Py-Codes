f = open("Q3.txt", "r").read()
txt = f.lower()
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
    txt = txt.replace(ch, " ")

words = txt.split()

finalwords = []
count = 0

for word in words:
    flag = True
    for x in word:
        for i in '1234567890!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
            if x == i:
                flag = False
    if flag:
        count += 1
        finalwords.append(word)

#print(words)
print(finalwords)
print(count)