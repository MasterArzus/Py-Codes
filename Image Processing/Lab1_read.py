import cv2
from PIL import Image, ImageEnhance
import numpy as np

# step 1 import the bmp picture
# img = cv2.imread('pic/lab1.bmp')
img_p = Image.open('pic/lab1.bmp')
img_arr = np.array(img_p)

# print(img_arr)

# step 2 split into 3 channels and get the arrays
r, g, b = img_p.split()
r_arr = np.array(r)
g_arr = np.array(g)
b_arr = np.array(b)

# step 3 change the color of r channel
r_arr_new = r_arr
mask = r_arr_new > 200
r_arr_new[mask] = 100
#print(r_arr)

# merge the channels
img1_arr = np.dstack((r_arr_new, g_arr, b_arr))
img1 = Image.fromarray(img1_arr)

# img1.save("lab1_f.bmp")

# convert it to YUV array
yuv_image = cv2.cvtColor(img_arr, cv2.COLOR_RGB2YUV)
y = 0.3*r_arr+0.59*g_arr+0.11*b_arr
u = 0.7*r_arr-0.59*g_arr-0.11*b_arr
v = -0.3*r_arr-0.59*g_arr+0.89*b_arr

# print(y,u,v)

# step 4 bright
enhancer = ImageEnhance.Brightness(img_p)
brightness_factor = 1.5  # 增加亮度
brighter_image = enhancer.enhance(brightness_factor)
# brighter_image.save("lab1_b.bmp")

# step 5 black

black_and_white_image = img_p.convert("L")
black_and_white_image.save("grey.bmp")
