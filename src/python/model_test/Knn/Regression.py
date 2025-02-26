import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 加载糖尿病数据集
diabetes = load_diabetes()
X = diabetes.data  # 特征
y = diabetes.target  # 目标值

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 标准化特征
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 创建KNN回归器，设置K=5
knn_reg = KNeighborsRegressor(n_neighbors=5)

# 训练模型
knn_reg.fit(X_train, y_train)

# 使用测试集进行预测
y_pred = knn_reg.predict(X_test)

# 计算均方误差（MSE）
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差 (MSE): {mse:.2f}")

# 计算决定系数（R²）
r2 = r2_score(y_test, y_pred)
print(f"决定系数 (R²): {r2:.2f}")