import cv2
import math
import  sys
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
import numpy as np

# step 1 import the bmp picture

def adjust_grayscale(image, factor):
    # Adjust grayscale by applying factor
    adjusted_img = image.point(lambda x: x * factor)
    return adjusted_img

def gammaTranform(c,gamma,image):
    h,w,d = image.shape[0],image.shape[1],image.shape[2]
    new_img = np.zeros((h,w,d),dtype=np.float32)
    for i in range(h):
        for j in range(w):
            new_img[i,j,0] = c*math.pow(image[i, j, 0], gamma)
            new_img[i,j,1] = c*math.pow(image[i, j, 1], gamma)
            new_img[i,j,2] = c*math.pow(image[i, j, 2], gamma)

    cv2.normalize(new_img,new_img,0,255,cv2.NORM_MINMAX)
    new_img = cv2.convertScaleAbs(new_img)
    new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB)

    return new_img

def gammaTranform2(c,gamma,image):
    h,w = image.shape[0],image.shape[1]
    new_img = np.zeros((h,w),dtype=np.float32)
    for i in range(h):
        for j in range(w):
            new_img[i,j] = c*math.pow(image[i, j], gamma)
            new_img[i,j] = c*math.pow(image[i, j], gamma)

    cv2.normalize(new_img,new_img,0,255,cv2.NORM_MINMAX)
    new_img = cv2.convertScaleAbs(new_img)
    new_img2 = cv2.cvtColor(new_img, cv2.IMREAD_GRAYSCALE)

    return new_img2



def main():
    # 1. Read BMP image content into a memory array
    grey = cv2.imread('pic/grey.bmp', cv2.IMREAD_GRAYSCALE)

    gamma = cv2.imread('pic/gamma.bmp')

    # 2. Adjust image grayscale and perform inverse transformation

    new_img1 = gammaTranform2(1, 1, grey)
    new_img2 = gammaTranform2(1, 0.8, grey)
    new_img3 = gammaTranform2(1, 0.6, grey)
    new_img4 = gammaTranform2(1, 0.4, grey)
    new_img5 = gammaTranform(1, 1, gamma)
    new_img6 = gammaTranform(1, 0.8, gamma)
    new_img7 = gammaTranform(1, 0.6, gamma)
    new_img8 = gammaTranform(1, 0.4, gamma)

    plt.subplot(241), plt.imshow(new_img1), plt.title("gamma = 1")
    plt.subplot(242), plt.imshow(new_img2), plt.title("gamma = 0.8")
    plt.subplot(243), plt.imshow(new_img3), plt.title("gamma = 0.6")
    plt.subplot(244), plt.imshow(new_img4), plt.title("gamma = 0.4")
    plt.subplot(245), plt.imshow(new_img5), plt.title("gamma = 1")
    plt.subplot(246), plt.imshow(new_img6), plt.title("gamma = 0.8")
    plt.subplot(247), plt.imshow(new_img7), plt.title("gamma = 0.6")
    plt.subplot(248), plt.imshow(new_img8), plt.title("gamma = 0.4")
    plt.show()

    # grayscale_factors = [1.0, 0.4, 0.6, 0.8]
    # for factor in grayscale_factors:
    #     adjusted_image = adjust_grayscale(gamma, factor)
    #
    #     # Save adjusted images
    #     adjusted_image.save(f"lab2_gamma_{factor}.bmp")

if __name__ == "__main__":
    main()
