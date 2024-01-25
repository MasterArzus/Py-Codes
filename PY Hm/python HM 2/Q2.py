import random
import string


def strip(str):
    l = 0
    r = len(str)

    for ch in "  \n \t":
        str = str.replace(ch, "")

    return str[l:r]


print(strip('\n\t  a\n b\tc\n'))
print(strip('       sdf \n jeknjwfo \t \n hjsf'))