# coding:utf-8
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel
# from qfluentwidgets import FluentIcon
import cv2
import numpy as np
# from views.Ui_reverseColorInterface import Ui_reverseColor_Interface


class reverseColor_Interface(Ui_reverseColor_Interface, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.imgpath = ''
        self.connect_process()
        self.init_slider()

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
        self.reverseColor_correct()

    def reverseColor_correct_help(self, image):
        # 获取高度和宽度
        height = image.shape[0]
        width = image.shape[1]

        # 生成一个空的相同尺寸的图像
        negative_image = np.zeros((height, width, 3))

        # 拆分三通道，注意顺序
        b, g, r = cv2.split(image)

        # 进行负片处理，求每个通道颜色的补色
        r = 255 - r
        b = 255 - b
        g = 255 - g

        # 将处理后的结果赋值到前面生成的三维张量
        negative_image[:, :, 0] = b
        negative_image[:, :, 1] = g
        negative_image[:, :, 2] = r

        return negative_image


    def reverseColor_correct(self):
        # 读取彩色
        img = cv2.imread(self.imgpath, cv2.IMREAD_COLOR)

        transformed_img = self.reverseColor_correct_help(img)

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
