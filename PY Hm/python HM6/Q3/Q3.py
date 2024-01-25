from PIL import Image
import numpy as np

bird = Image.open('bird.jpg')
pic1 = Image.open('1.jpg')
pic2 = Image.open('2.jpg')
pic3 = Image.open('3.jpg')
pic4 = Image.open('4.jpg')
pic5 = Image.open('5.jpg')
pic6 = Image.open('6.jpg')

gray_bird = bird.convert('L')

for y in range(0, 544, 16):
    for x in range(0, 544, 16):
        low = y + 16
        right = x + 16
        c = gray_bird.crop((x, y, right, low))
        gray = np.mean(c)
        if gray < 10:
            gray_bird.paste(pic6, (x, y, right, low))
        elif 10 <= gray < 86:
            gray_bird.paste(pic5, (x, y, right, low))
        elif 86 <= gray < 155:
            gray_bird.paste(pic4, (x, y, right, low))
        elif 155 <= gray < 230:
            gray_bird.paste(pic3, (x, y, right, low))
        elif 230 <= gray < 240:
            gray_bird.paste(pic2, (x, y, right, low))
        else:
            gray_bird.paste(pic1, (x, y, right, low))

gray_bird.save('PixelBird.jpg')
