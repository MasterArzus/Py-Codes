import cv2
import numpy as np


def Gaussian_low_pass_filter(original_image, sigma=1):
    # Apply Gaussian filter
    filtered_image = cv2.GaussianBlur(original_image, (0, 0), sigma)
    return filtered_image


def Butterworth_low_pass_filter(original_image, cutoff_frequency=10, order=2):
    # Calculate the size of the Butterworth filter kernel
    rows, cols = original_image.shape
    # crow, ccol = rows // 2, cols // 2

    u = np.fft.fftshift(np.fft.fftfreq(rows))
    v = np.fft.fftshift(np.fft.fftfreq(cols))

    # Generate a Butterworth low-pass filter kernel
    butterworth_filter = 1 / ((1 + (u ** 2 + v ** 2) / cutoff_frequency ** 2) ** order)

    # Apply the Butterworth filter to the image
    original_image_fft = np.fft.fft2(original_image)
    filtered_image_fft = original_image_fft * butterworth_filter
    filtered_image = np.fft.ifft2(filtered_image_fft).real

    return filtered_image


def Gaussian_High_pass_filter(original_image, sigma=1):
    # Apply Gaussian filter
    low_pass_filtered = cv2.GaussianBlur(original_image, (0, 0), sigma)
    # Calculate the high-pass filtered image
    high_pass_filtered = original_image - low_pass_filtered

    return high_pass_filtered


def Butterworth_high_pass_filter(original_image, cutoff_frequency=30, order=2):
    # Calculate the size of the Butterworth filter kernel
    rows, cols = original_image.shape
    # crow, ccol = rows // 2, cols // 2

    u = np.fft.fftshift(np.fft.fftfreq(rows))
    v = np.fft.fftshift(np.fft.fftfreq(cols))

    # Generate a Butterworth high-pass filter kernel
    butterworth_filter = 1 / (1 + (u ** 2 + v ** 2) / cutoff_frequency ** 2) ** order

    # Apply the Butterworth filter to the image
    original_image_fft = np.fft.fft2(original_image)
    filtered_image_fft = original_image_fft * butterworth_filter
    filtered_image = np.fft.ifft2(filtered_image_fft).real

    return filtered_image


def main():
    # 1. Read BMP image content into a memory array
    img = cv2.imread("pic/lab5-1.bmp", cv2.IMREAD_COLOR)
    img_2 = cv2.imread("pic/lab5-2.bmp", cv2.IMREAD_COLOR)

    # 2. Apply mean filter to remove noise
    Gl_image = Gaussian_low_pass_filter(img,1.2)
    cv2.imwrite("result/lab5_Gl_image.bmp", Gl_image)

    # 3. Apply median filter to remove noise
    GH_image = Gaussian_High_pass_filter(img_2, 0.35)
    cv2.imwrite("result/lab5_GH_image.bmp", GH_image)

    # 2. Apply mean filter to remove noise
    Bl_image = Gaussian_low_pass_filter(img,0.8)
    cv2.imwrite("result/lab5_Bl_image.bmp", Bl_image)

    # 3. Apply median filter to remove noise
    BH_image = Gaussian_High_pass_filter(img_2, 0.4)
    cv2.imwrite("result/lab5_BH_image.bmp", BH_image)

    print("Image processing completed.")

if __name__ == "__main__":
    main()
