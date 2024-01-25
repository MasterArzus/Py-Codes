import turtle

"""
可能使用到的函数：
turtle.setup：四个参数分别为，窗口的宽度、高度，窗口距离屏幕左边的像素值，
窗口距离屏幕上边的像素值，比如turtle.setup(500, 500, 50, 50)，打开一个500×500的窗口，该窗口距离屏幕左边50像素，距离上边50像素。
turtle.forward: 将turtle向前方移动，参数为移动的距离。
turtle.backward：类似于turtle.forward。
turtle.left: 将turtle向左转动移动角度，参数为旋转的角度。
turtle.right: 类似于turtle.left。
turtle.done: 让程序进入循环，保持窗口，写在程序的最后。
大致思路：首先绘制一个正方形，然后将turtle旋转一定角度，再次绘制等大小的正方形，重复以上步骤。
"""


def DrawSquare():
    turtle.pendown()
    x = 0
    while x < 4:
        turtle.fd(100)
        turtle.right(90)
        x = x + 1
    turtle.penup()


def main():
    turtle.setup(700, 700, 100, 100)
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.right(180)
    turtle.pensize(2)
    x = 0
    while x < 24:
        DrawSquare()
        turtle.left(15)
        x = x + 1
    turtle.done()


main()
