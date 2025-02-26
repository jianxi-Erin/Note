import cv2 as cv

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

