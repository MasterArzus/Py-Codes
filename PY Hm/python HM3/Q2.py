# 在下面自行定义strip函数
def strip(str, side="both", blanks=['\t', '\n', ' ']):
    i = 0
    j = len(str) - 1
    if side == 'both':
        find = True
        while find == True:
            find = False
            for k in blanks:
                if str[i] == k:
                    i += 1
                    find = True
        find = True
        while find == True:
            find = False
            for k in blanks:
                if str[j] == k:
                    j -= 1
                    find = True
    if side == 'left':
        find = True
        while find == True:
            find = False
            for k in blanks:
                if str[i] == k:
                    i += 1
                    find = True
    if side == 'right':
        find = True
        while find == True:
            find = False
            for k in blanks:
                if str[j] == k:
                    j -= 1
                    find = True
    return str[i:j + 1]


# 供测试的语句如下：
print("\"" + strip("   abc   ") + "\"")
print("\"" + strip("   abc   ", "both") + "\"")
print("\"" + strip("   abc   ", "left") + "\"")
print("\"" + strip("   abc   ", side="right") + "\"")
print("\"" + strip("aaadefccc  ", blanks=["a", "c", " "]) + "\"")
