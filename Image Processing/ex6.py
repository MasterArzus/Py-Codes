import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft2, ifft2, fftshift, ifftshift


def apply_fourier_transform(image):
    # 进行二维FFT
    spectrum = fft2(image)
    spectrum_shifted = fftshift(spectrum)
    return spectrum_shifted


def apply_inverse_fourier_transform(spectrum):
    # 进行二维逆FFT
    inverted_spectrum = ifftshift(spectrum)
    inverted_image = np.abs(ifft2(inverted_spectrum))
    return inverted_image


def inverse_filter(spectrum, kernel):
    # 频域逆滤波
    inverted_spectrum = spectrum / (kernel + 1e-8)
    return inverted_spectrum


def weiner_filter(spectrum, kernel, alpha):
    # 维纳滤波
    inverted_spectrum = spectrum * np.conj(kernel) / (np.abs(kernel) ** 2 + alpha)
    return inverted_spectrum


def generate_degradation_function(shape, k):
    rows, cols = shape
    center_row, center_col = rows // 2, cols // 2
    u, v = np.meshgrid(np.arange(rows) - center_row, np.arange(cols) - center_col)
    degradation_function = np.exp(-k * (u ** 2 + v ** 2) ** (5 / 6))
    return degradation_function


def main():
    # 读入图像
    image_path = 'pic/Lab6-1.bmp'
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 进行二维FFT
    spectrum = apply_fourier_transform(original_image)

    k_value = 1  # 根据实际情况调整
    degradation_function_inverse = generate_degradation_function(spectrum.shape, k_value)

    # 进行频域逆滤波
    inverse_filtered_spectrum = inverse_filter(spectrum, degradation_function_inverse)

    # 进行频域维纳滤波
    k_value = 1e-3
    degradation_function_weiner = generate_degradation_function(spectrum.shape, k_value)
    alpha = 1e-2  # 维纳滤波的参数，需要根据具体情况调整
    weiner_filtered_spectrum = weiner_filter(spectrum, degradation_function_weiner, alpha)

    # 进行二维逆FFT得到复原图像
    inverse_filtered_image = apply_inverse_fourier_transform(inverse_filtered_spectrum)
    weiner_filtered_image = apply_inverse_fourier_transform(weiner_filtered_spectrum)

    # 显示原始图像和复原图像
    plt.figure(figsize=(12, 8))

    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(inverse_filtered_image, cmap='gray')
    plt.title('Inverse Filtered Image')

    plt.subplot(1, 3, 3)
    plt.imshow(weiner_filtered_image, cmap='gray')
    plt.title('Weiner Filtered Image')

    plt.tight_layout()
    plt.savefig('result/Lab6.png')  # 保存图像
    plt.show()


if __name__ == "__main__":
    main()
