import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读入图片
img = cv2.imread( "pic/Lab7-1.bmp")

# 转换颜色空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 提取hsv中H通道数据
h = hsv[:, :, 0].ravel()
# 直方图显示
plt.hist(h, 180, [0, 180])
plt.show()

# 定义绿色范围
lower_blue = np.array([75, 50, 50])
upper_blue = np.array([120, 255, 255])

# 定义黄色范围
lower_skin = np.array([0, 15, 50])
upper_skin = np.array([25, 255, 255])

lower_skin2 = np.array([175, 180, 50])
upper_skin2 = np.array([180, 255, 255])

# 根据颜色范围创建掩码
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_skin = cv2.inRange(hsv, lower_skin, upper_skin)
mask_skin2 = cv2.inRange(hsv, lower_skin2, upper_skin2)
mask = cv2.bitwise_or(mask_skin, mask_skin2)

# 应用掩码
result = cv2.bitwise_and(img, img, mask=mask_blue)
result = img - result
result2 = cv2.bitwise_or(img, img, mask=mask)

# 显示结果
plt.subplot(1, 3, 1)
show_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(show_img)
plt.title('Original Image')

plt.subplot(1, 3, 2)
show_img2 = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
plt.imshow(show_img2)
plt.title('Processed Image')

plt.subplot(1, 3, 3)
show_img3 = cv2.cvtColor(result2, cv2.COLOR_BGR2RGB)
plt.imshow(show_img3)
plt.title('Processed Image2')

plt.tight_layout()
# plt.savefig('result/Lab7-2.png')  # 保存图像
plt.show()