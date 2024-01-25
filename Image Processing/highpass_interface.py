# coding:utf-8
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel
# from qfluentwidgets import FluentIcon
import cv2
import numpy as np
from views.Ui_HighpassInterface import Ui_Highpass_Interface

class HighPass_Interface(Ui_HighPass_Interface, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.imgpath = ''
        self.sigma = 1.0
        self.connect_process()
        self.init_slider()

    def init_slider(self):
        self.slider.setMinimum(1)
        self.slider.setMaximum(200)
        self.slider.setValue(100)
        text = str(self.sigma)
        self.value_label.setText(text)
        self.slider.valueChanged.connect(self.slider_change)

    def slider_change(self):
        self.sigma = self.slider.value() / 100
        self.value_label.setText(str(self.sigma))
        if self.imgpath == '':
            return
        else:
            self.Gaussian_High_pass_filter()

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
        self.Gaussian_High_pass_filter()

    def Gaussian_High_pass_filter_help(self, original_image, sigma=1):
        # Apply Gaussian filter
        low_pass_filtered = cv2.GaussianBlur(original_image, (0, 0), sigma)
        # Calculate the high-pass filtered image
        high_pass_filtered = original_image - low_pass_filtered

        return high_pass_filtered

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

    def Gaussian_High_pass_filter(self):
        # 读取彩色
        img = cv2.imread(self.imgpath, cv2.IMREAD_COLOR)
        alpha = self.slider.value() / 100

        transformed_img = self.Gaussian_High_pass_filter_help(img, alpha)

        self.show_transformed_image(transformed_img)


    def Butterworth_high_pass_filter(self, original_image, cutoff_frequency=10, order=2):
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