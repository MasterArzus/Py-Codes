class BigNum(object):

    def __init__(self, num):
        if num[0] == '-':
            temp_num = num[1:]
            while temp_num[0] == "0":
                if len(temp_num) == 1:
                    break
                temp_num = temp_num[1:]

            self.num = temp_num
            self.sign = -1  # 代表负数
        else:
            temp_num = num
            while temp_num[0] == "0":
                if len(temp_num) == 1:
                    break
                temp_num = temp_num[1:]

            self.num = temp_num
            self.sign = 1  # 代表正数

    def __str__(self):
        if self.num == '0':
            return '0'
        elif len(self.num) > 20 and self.sign > 0:
            return 'Infinity'
        elif len(self.num) > 20 and self.sign < 0:
            return '-Infinity'
        elif self.sign < 0:
            return '-' + self.num
        else:
            return self.num

    def addition(self, other):
        sum_result = []
        length = max(len(self.num), len(other.num))
        is_add = False  # 是否向前进一位
        for index in range(-1, -length - 1, -1):
            x = 0 if index < -len(self.num) else int(self.num[index])
            y = 0 if index < -len(other.num) else int(other.num[index])
            r = x + y
            if is_add:
                r += 1
            if r <= 9:
                is_add = False
                sum_result.append(r)
            else:
                # 大于10向前进一位
                is_add = True
                sum_result.append(r % 10)

        sum_result.reverse()
        sum_result_string = "".join(str(x) for x in sum_result)

        return BigNum(sum_result_string)

    def subtraction(self, other):
        sub_result = []
        if len(self.num) < len(other.num):
            sign = -1
            numX = other.num
            numY = self.num
        elif len(self.num) == len(other.num) and int(self.num[0]) < int(other.num[0]):
            sign = -1
            numX = other.num
            numY = self.num
        else:
            sign = 1
            numX = self.num
            numY = other.num

        length = max(len(numX), len(numY))
        is_sub = False  # 是否向后补一位

        for index in range(-1, -length - 1, -1):
            x = 0 if index < -len(numX) else int(numX[index])
            y = 0 if index < -len(numY) else int(numY[index])
            r = x - y
            if is_sub:
                r -= 1
            if r >= 0:
                is_sub = False
                sub_result.append(r)
            else:
                # 不够减向前补一位
                is_sub = True
                sub_result.append(10 + r)

        sub_result.reverse()
        sum_result_string = "".join(str(x) for x in sub_result)

        temp_num = BigNum(sum_result_string)
        temp_num.sign = sign

        return temp_num

    def __add__(self, other):
        if self.sign > 0 and other.sign > 0:
            return BigNum.addition(self, other)
        elif self.sign > 0 and other.sign < 0:
            return BigNum.subtraction(self, other)
        elif self.sign < 0 and other.sign > 0:
            return BigNum.subtraction(other, self)
        elif self.sign < 0 and other.sign < 0:
            temp_num = BigNum.addition(self, other)
            temp_num.sign = -1
            return temp_num

    def __sub__(self, other):
        if self.sign > 0 and other.sign > 0:
            return BigNum.subtraction(self, other)
        elif self.sign > 0 and other.sign < 0:
            return BigNum.addition(self, other)
        elif self.sign < 0 and other.sign > 0:
            temp_num = BigNum.addition(self, other)
            temp_num.sign = -1
            return temp_num
        elif self.sign < 0 and other.sign < 0:
            return BigNum.subtraction(other, self)

    def __and__(self, other):
        if self.num == other.num and self.sign == other.sign:
            return 0
        if self.sign < other.sign:
            return -1
        if self.sign > other.sign:
            return 1
        if self.sign == 1 and other.sign == 1:
            if len(self.num) > len(other.num):
                return 1
            if len(self.num) < len(other.num):
                return -1
            if len(self.num) == len(other.num):
                for i in range(0, len(self.num) - 1):
                    if self.num[i] < other.num[i]:
                        return -1
                    if self.num[i] > other.num[i]:
                        return 1
        if self.sign == -1 and other.sign == -1:
            if len(self.num) < len(other.num):
                return 1
            if len(self.num) > len(other.num):
                return -1
            if len(self.num) == len(other.num):
                for i in range(0, len(self.num) - 1):
                    if self.num[i] > other.num[i]:
                        return -1
                    if self.num[i] < other.num[i]:
                        return 1


number1 = BigNum('1234567890')
number6 = BigNum('1234567865')
number2 = BigNum('-81234567890')
number3 = BigNum('00000000200')
number4 = BigNum('100000000000000000000')
number5 = BigNum('-100000000000000000000')

print(number1)
print(number2)

print(number1 + number2)
print(number1 - number2)

print(number1 & number6)

print(number3)
print(number4)
print(number5)
