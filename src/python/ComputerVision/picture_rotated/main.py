import cv2
import numpy as np
import matplotlib.pyplot as plt

# import matplotlib as plt
image=cv2.imread("img.png")

# 转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用Canny边缘检测
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# 使用HoughLines检测直线
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# 计算旋转角度
angles = []
for line in lines:
    rho, theta = line[0]
    angle = np.degrees(theta)
    angles.append(angle)

# 计算平均角度
median_angle = np.median(angles)

# 计算需要旋转的角度
if median_angle < 45:
    rotation_angle = median_angle
else:
    rotation_angle = median_angle - 90

# 获取图片中心点
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# 计算旋转矩阵
M = cv2.getRotationMatrix2D(center, rotation_angle, 1.0)

# 执行旋转
rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
rotated = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
# 显示结果
# 显示原始图像
plt.subplot(1, 2, 1)  # 1行2列，第1个子图
plt.imshow(image)
plt.title('Original Image')

# 显示旋转后的图像
plt.subplot(1, 2, 2)  # 1行2列，第2个子图
plt.imshow(rotated)
plt.title('Rotated Image')

# 显示图像
plt.tight_layout()  # 自动调整子图间距
plt.show()