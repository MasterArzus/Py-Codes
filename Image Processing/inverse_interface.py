# coding:utf-8
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel
# from qfluentwidgets import FluentIcon
import cv2
import numpy as np
from numpy.fft import fft2, ifft2, fftshift, ifftshift
# from views.Ui_InverseInterface import Ui_Inverse_Interface

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


def Inverse_filter(spectrum, kernel, alpha):
    # 维纳滤波
    inverted_spectrum = spectrum * np.conj(kernel) / (np.abs(kernel) ** 2 + alpha)
    return inverted_spectrum


def generate_degradation_function(shape, k):
    rows, cols = shape
    center_row, center_col = rows // 2, cols // 2
    u, v = np.meshgrid(np.arange(rows) - center_row, np.arange(cols) - center_col)
    degradation_function = np.exp(-k * (u ** 2 + v ** 2) ** (5 / 6))
    return degradation_function

class Inverse_Interface(Ui_Inverse_Interface, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.imgpath = ''
        self.Inverse = 1.0
        self.connect_process()
        self.init_slider()

    def init_slider(self):
        self.slider.setMinimum(1)
        self.slider.setMaximum(200)
        self.slider.setValue(100)
        text = str(self.Inverse)
        self.value_label.setText(text)
        self.slider.valueChanged.connect(self.slider_change)

    def slider_change(self):
        self.Inverse = self.slider.value() / 100
        self.value_label.setText(str(self.Inverse))
        if self.imgpath == '':
            return
        else:
            self.Inverse_correct()

    def connect_process(self):
        btn_open = self.openfile_button
        btn_open.clicked.connect(self.open_file)

    def open_file(self):
        directory = QFileDialog.getOpenFileName(self,
                                                "getOpenFileName", "./",
                                                "BMP Files (*.bmp);;JPEG Files (*.jpg);;PNG Files (*.png)")
        self.imgpath = directory[0]
        if self.imgpath == '':
            return
        jpg = QtGui.QPixmap(self.imgpath).scaled(self.original_pic.width(), self.original_pic.height())


        self.original_pic.setPixmap(jpg)
        self.Inverse_correct()

    def Inverse_correct_help(self, image, k_value = 1 ):
        # 进行二维FFT
        spectrum = apply_fourier_transform(image)

        # k_value = 1  根据实际情况调整
        degradation_function_inverse = generate_degradation_function(spectrum.shape, k_value)

        # 进行频域逆滤波
        inverse_filtered_spectrum = inverse_filter(spectrum, degradation_function_inverse)

        # 进行二维逆FFT得到复原图像
        inverse_filtered_image = apply_inverse_fourier_transform(inverse_filtered_spectrum)
        return inverse_filtered_image

    def Inverse_correct(self):
        # 读取彩色
        img = cv2.imread(self.imgpath, cv2.IMREAD_COLOR)
        alpha = self.slider.value() / 100

        transformed_img = self.Inverse_correct_help(img, alpha)

        self.show_transformed_image(transformed_img)


    def show_transformed_image(self, transformed_img):
        # 将th在线显示到transform_pic
        th_rgb = cv2.cvtColor(transformed_img, cv2.COLOR_BGR2RGB)
        th_resized = cv2.resize(th_rgb, (self.transform_pic.width(), self.transform_pic.height()))

        # 将OpenCV格式的图像转换为Qt格式的图像
        height, width, channel = th_resized.shape
        bytes_per_line = 3 * width
        q_image = QImage(th_resized.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # 将QImage转换为QPixmap并设置到transform_pic上
        pixmap = QPixmap.fromImage(q_image)
        self.transform_pic.setPixmap(pixmap)

    def Inverse_correct(self):
        # 读取彩色
        img = cv2.imread(self.imgpath, cv2.IMREAD_COLOR)
        alpha = self.slider.value() / 100

        transformed_img = self.Inverse_correct_help(img, alpha)

        self.show_transformed_image(transformed_img)
