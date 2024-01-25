import math


class Vector2D(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __str__(self):
        return f'The coordinates of the point is x={self.x} and y={self.y}'

    def angle(self, other):
        result = math.acos(self * other / round(abs(self) * abs(other), 2))
        return f'The angle between 2 vector is {result}'


a = Vector2D(1, 2)
b = Vector2D(2, 3)
print(a + b)
print('The multiplication of 2 vector is ')
print(a * b)
print(b - a)
print('The vector module length is ')
print(abs(a))
print(str(b))
print(a.angle(b))
