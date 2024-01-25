from PIL import Image
import numpy as np

bird = Image.open('bird.jpg')

gray_bird = bird.convert('L')

bird_line = ''

for y in range(0, 544, 16):
    for x in range(0, 544, 16):
        low = y + 16
        right = x + 16
        c = gray_bird.crop((x, y, right, low))
        gray = np.mean(c)
        if gray < 115:
            bird_line += ' □'
        else:
            bird_line += ' ■'
    bird_line += '\n'

fw = open('bird.txt', 'w', encoding='UTF-8')
fw.write(bird_line)
fw.close()
