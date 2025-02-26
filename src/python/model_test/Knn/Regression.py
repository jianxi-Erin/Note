import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error,r2_score

# 加载加利福尼亚房价数据集
california = fetch_california_housing()
X = california.data  # 特征数据
y = california.target  # 目标变量（房价）

# 查看数据集信息
print("特征数据形状:", X.shape)
print("目标变量形状:", y.shape)
print("特征名称:", california.feature_names)
print("数据集描述:\n", california.DESCR)

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化KNN回归模型
knn_regressor = KNeighborsRegressor(n_neighbors=5)  # 使用5个邻居

# 训练模型
knn_regressor.fit(X_train, y_train)

# 预测测试集
y_pred = knn_regressor.predict(X_test)

# 评估模型性能
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("均方误差 (MSE):", mse)
print("R^2 分数:", r2)

# 可视化预测结果 vs 真实值
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')  # 绘制对角线
plt.xlabel("真实值")
plt.ylabel("预测值")
plt.title("KNN回归预测结果 vs 真实值")
plt.show()