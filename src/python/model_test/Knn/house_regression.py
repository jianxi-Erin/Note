# 导入必要库
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 加载数据
housing = fetch_california_housing()
X = housing.data  # 特征
y = housing.target  # 目标值（房价中位数的对数变换值）
feature_names = housing.feature_names

# 数据标准化（KNN对特征尺度敏感）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 网格搜索
# grid_search = GridSearchCV(KNeighborsRegressor(), param_grid, cv=5, scoring='neg_mean_squared_error')
# grid_search.fit(X_train, y_train)

# # 输出最优参数
# print("最优邻居数：", grid_search.best_params_['n_neighbors'])
# print("最优MSE：", -grid_search.best_score_)

# 训练KNN回归模型
knn_reg = KNeighborsRegressor(n_neighbors=11,metric='manhattan')  # 使用11个最近邻,使用曼哈顿距离
knn_reg.fit(X_train, y_train)

# 预测
y_pred = knn_reg.predict(X_test)

# 评估模型
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"均方误差（MSE）：{mse:.2f}")
print(f"R²分数：{r2:.2f}")

from sklearn.model_selection import GridSearchCV

# 参数网格
param_grid = {'n_neighbors': range(1, 20)}


# 可视化预测结果 vs 真实值
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)  # 绘制对角线
plt.xlabel("真实值")
plt.ylabel("预测值")
plt.title("KNN回归：真实值 vs 预测值")
plt.show()

# 残差分析
residuals = y_test - y_pred
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--', lw=2)  # 绘制水平线
plt.xlabel("预测值")
plt.ylabel("残差")
plt.title("残差分析")
plt.show()