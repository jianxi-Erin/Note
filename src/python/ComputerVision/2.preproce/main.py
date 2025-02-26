import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
image = cv2.imread("paimeng.png")

# 检查图片是否成功加载
if image is None:
    print("图片加载失败，请检查路径是否正确")
    exit()

# 将 BGR 图像转换为 RGB（Matplotlib 使用 RGB 格式）
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 图像灰度化
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 图像缩放
resized_image = cv2.resize(image_rgb, (300, 200))  # 宽度 300，高度 200

# 图像裁剪 (ROI: Region of Interest)
cropped_image = image_rgb[50:200, 100:300]  # y1:y2, x1:x2

# 图像旋转
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
angle = 45  # 旋转角度
M_rotate = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_image = cv2.warpAffine(image_rgb, M_rotate, (w, h))

# 图像翻转 (水平翻转)
flipped_image = cv2.flip(image_rgb, 1)

# 图像二值化
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# 图像去噪 (高斯滤波)
denoised_image = cv2.GaussianBlur(image_rgb, (5, 5), 0)

# 边缘检测 (Canny 边缘检测)
edges = cv2.Canny(gray_image, 100, 200)

# 直方图均衡化
equalized_image = cv2.equalizeHist(gray_image)

# 图像平移
M_translate = np.float32([[1, 0, 50], [0, 1, 30]])  # 向右平移 50，向下平移 30
translated_image = cv2.warpAffine(image_rgb, M_translate, (w, h))

# 图像剪切 (仿射变换)
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])  # 原始图像中的三个点
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])  # 变换后的三个点
M_shear = cv2.getAffineTransform(pts1, pts2)
sheared_image = cv2.warpAffine(image_rgb, M_shear, (w, h))

# 图像仿射变换
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])  # 原始图像中的三个点
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])  # 变换后的三个点
M_affine = cv2.getAffineTransform(pts1, pts2)
affine_image = cv2.warpAffine(image_rgb, M_affine, (w, h))

# 图像透视变换
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])  # 原始图像中的四个点
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])  # 变换后的四个点
M_perspective = cv2.getPerspectiveTransform(pts1, pts2)
perspective_image = cv2.warpPerspective(image_rgb, M_perspective, (300, 300))

# 使用 Matplotlib 展示每一步骤的效果
plt.figure(figsize=(20, 15))

# 原始图像
plt.subplot(4, 4, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

# 灰度图像
plt.subplot(4, 4, 2)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

# 缩放图像
plt.subplot(4, 4, 3)
plt.imshow(resized_image)
plt.title("Resized Image")
plt.axis('off')

# 裁剪图像
plt.subplot(4, 4, 4)
plt.imshow(cropped_image)
plt.title("Cropped Image")
plt.axis('off')

# 旋转图像
plt.subplot(4, 4, 5)
plt.imshow(rotated_image)
plt.title("Rotated Image")
plt.axis('off')

# 翻转图像
plt.subplot(4, 4, 6)
plt.imshow(flipped_image)
plt.title("Flipped Image")
plt.axis('off')

# 二值化图像
plt.subplot(4, 4, 7)
plt.imshow(binary_image, cmap='gray')
plt.title("Binary Image")
plt.axis('off')

# 去噪图像
plt.subplot(4, 4, 8)
plt.imshow(denoised_image)
plt.title("Denoised Image")
plt.axis('off')

# 边缘检测
plt.subplot(4, 4, 9)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.axis('off')

# 直方图均衡化
plt.subplot(4, 4, 10)
plt.imshow(equalized_image, cmap='gray')
plt.title("Histogram Equalization")
plt.axis('off')

# 平移图像
plt.subplot(4, 4, 11)
plt.imshow(translated_image)
plt.title("Translated Image")
plt.axis('off')

# 剪切图像
plt.subplot(4, 4, 12)
plt.imshow(sheared_image)
plt.title("Sheared Image")
plt.axis('off')

# 仿射变换图像
plt.subplot(4, 4, 13)
plt.imshow(affine_image)
plt.title("Affine Transform")
plt.axis('off')

# 透视变换图像
plt.subplot(4, 4, 14)
plt.imshow(perspective_image)
plt.title("Perspective Transform")
plt.axis('off')

# 调整子图间距
plt.tight_layout()

# 显示图像
plt.show()