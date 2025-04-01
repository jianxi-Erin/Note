import cv2 as cv
# 1. 读取图像
# 参数:
#   - filename: 图像文件路径
#   - flags: 读取模式，可选：
#       - cv2.IMREAD_COLOR (默认): 读取为彩色图像 (3通道)
#       - cv2.IMREAD_GRAYSCALE: 读取为灰度图像 (1通道)
#       - cv2.IMREAD_UNCHANGED: 读取包含透明通道的图像 (4通道)
# 返回值：
# - 图像矩阵（H×W×C 格式）
image=cv.imread("img/paimeng.png")
# 检查图片是否成功加载
if image is None:
    print("图片加载失败，请检查路径是否正确")
else:
    # 显示图片
    cv.imshow('Image', image)
    cv.waitKey(0)  # 等待按键按下
    cv.destroyAllWindows()  # 关闭所有窗口
    # 保存图片
    # cv.imwrite('paimeng.jpg', image)

# 或者使用matplotlib显示图像
# import matplotlib.pyplot as plt
# plt.imshow(image[:, :, ::-1])
# plt.axis('off')
# plt.show()

