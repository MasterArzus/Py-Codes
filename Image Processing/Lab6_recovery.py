import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread('pic/Lab6-1.bmp',0)

# 进行傅里叶变换
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

#-------------利用大气湍流模型估计退化传递函数-----------------
k = 0.001  #湍流程度
degeneration = np.zeros(fshift.shape,dtype=complex)
for u in range(fshift.shape[0]):
    for v in range(fshift.shape[1]):
        H = np.exp(-k*np.power(np.float64((u+fshift.shape[0]//2)**2+(v-fshift.shape[1]//2)**2),5/6))
        degeneration[u][v] =  H
#-----------------------------------------

def recovery1(fshift, degeneration):
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    d = 30  # 滤波器大小
    butter = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            butter[i, j] = 1 / (1 + np.power((np.power((i - crow) ** 2 + (j - ccol) ** 2, 0.5) / d), 20))

    fshift = np.multiply(fshift, butter)
    # 逆滤波
    img1 = np.divide(fshift, butter)

    # 将频域图像在空域进行显示做的处理
    img1 = np.fft.ifftshift(img1)
    img1 = np.fft.ifft2(img1)
    img1 = np.abs(img1)
    img1 = cv2.normalize(img1, None, 0, 1, cv2.NORM_MINMAX)
    return img1


def recovery2(fshift, degeneration):
    # 维纳滤波
    K = 0.001
    degeneration += 0.1  # 加上估计的噪声
    img1 = (np.conj(degeneration) / (np.conj(degeneration) * degeneration + K)) * fshift

    # 将频域图像在空域进行显示做的处理
    img1 = np.fft.ifftshift(img1)
    img1 = np.fft.ifft2(img1)
    img1 = np.abs(img1)
    img1 = cv2.normalize(img1, None, 0, 1, cv2.NORM_MINMAX)
    return img1


def main():

    # 显示原始图像和恢复后的图像
    plt.figure(figsize=(20, 20))
    plt.subplot(131), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(recovery1(fshift, degeneration), cmap='gray')
    plt.title('rec img1'), plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(recovery2(fshift, degeneration), cmap='gray')
    plt.title('rec img2'), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()


