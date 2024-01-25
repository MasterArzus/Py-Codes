from PIL import Image
import numpy as np
a = Image.open("bird.jpg")
p1 = Image.open('1.jpg')
p2 = Image.open('2.jpg')
p3 = Image.open('3.jpg')
p4 = Image.open('4.jpg')
p5 = Image.open('5.jpg')
p6 = Image.open('6.jpg')
a = a.convert('L')

for upper in range(0,544,16):
    for left in range(0, 544, 16):
        low = upper+16
        right= left+16
        c = a.crop((left, upper, right, low))
        gray = np.mean(c)  
        if gray < 10:
            a.paste(p6,(left, upper, right, low))
        elif gray >= 10 and gray < 86:
            a.paste(p5,(left, upper, right, low))
        elif gray >= 86 and gray < 155:
            a.paste(p4,(left, upper, right, low))
        elif gray >= 155 and gray < 230:
            a.paste(p3,(left, upper, right, low))
        elif gray >= 230 and gray < 240:
            a.paste(p2,(left, upper, right, low))
        else:
            a.paste(p1,(left, upper, right, low))
#p2new.save("p2new,jpg")
#for i in range(0, 544):
#    box = (i, 544, i+16, 552)
#    a.paste(p2new, box)
a.save('finalBird.jpg')
