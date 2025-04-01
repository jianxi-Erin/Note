import numpy as np

# 定义 Sobel 算子
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel_y = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]])

# 定义图像矩阵
I = np.array([[12, 15, 18, 20, 22, 25, 28],
              [16, 19, 21, 23, 26, 29, 32],
              [20, 22, 24, 27, 30, 33, 36],
              [24, 26, 28, 31, 34, 37, 40],
              [28, 30, 32, 35, 38, 41, 44],
              [32, 34, 36, 39, 42, 45, 48],
              [36, 38, 40, 43, 46, 49, 52]])

# 初始化梯度矩阵
gradient_x = np.zeros_like(I, dtype=float)
gradient_y = np.zeros_like(I, dtype=float)
gradient_magnitude = np.zeros_like(I, dtype=float)

# 计算梯度
for i in range(1, I.shape[0]-1):
    for j in range(1, I.shape[1]-1):
        # 提取 3x3 区域
        region = I[i-1:i+2, j-1:j+2]
        # 计算 x 方向梯度
        gradient_x[i, j] = np.sum(region * sobel_x)
        # 计算 y 方向梯度
        gradient_y[i, j] = np.sum(region * sobel_y)
        # 计算梯度幅值
        gradient_magnitude[i, j] = np.sqrt(gradient_x[i, j]**2 + gradient_y[i, j]**2)

# 输出结果
print("Gradient in X direction:")
print(gradient_x[1:-1, 1:-1])

print("Gradient in Y direction:")
print(gradient_y[1:-1, 1:-1])

print("Gradient Magnitude:")
print(gradient_magnitude[1:-1, 1:-1])