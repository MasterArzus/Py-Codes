# coding:utf-8
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel
# from qfluentwidgets import FluentIcon
import cv2
import numpy as np
# from views.Ui_LaplacianInterface import Ui_Laplacian_Interface


class Laplacian_Interface(Ui_Laplacian_Interface, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.imgpath = ''
        self.Laplacian_core = 0.7
        self.connect_process()
        self.init_slider()

    def init_slider(self):
        self.slider.setMinimum(1)
        self.slider.setMaximum(200)
        self.slider.setValue(70)
        text = str(self.Laplacian_core)
        self.value_label.setText(text)
        self.slider.valueChanged.connect(self.slider_change)

    def slider_change(self):
        self.Laplacian_core = self.slider.value() / 100
        self.value_label.setText(str(self.Laplacian_core))
        if self.imgpath == '':
            return
        else:
            self.Laplacian_correct()

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
        self.Laplacian_correct()

    def Laplacian_correct_help(self, image, Laplacian_core = 0.7):
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply the Laplacian filter
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)

        # Convert the Laplacian result back to 8-bit unsigned integer
        sharpened = np.uint8(np.clip(gray - Laplacian_core * laplacian, 0, 255))

        # Create a merged image with the original and sharpened versions
        corrected_image = cv2.merge((sharpened, sharpened, sharpened))

        return corrected_image


    def Laplacian_correct(self):
        # 读取彩色
        img = cv2.imread(self.imgpath, cv2.IMREAD_COLOR)
        alpha = self.slider.value() / 100

        transformed_img = self.Laplacian_correct_help(img, alpha)

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

