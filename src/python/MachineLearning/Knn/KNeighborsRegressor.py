# 使用KNN模型预测加州房价回归问题
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
# 加载加州房价数据集
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
print("=== KNN回归模型评估 ===")
print(f"均方误差（MSE）：{mse:.2f}")
print(f"R²分数：{r2:.2f}")


# 随机网格调优
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# 定义参数分布空间
param_dist = {
    'n_neighbors': randint(1, 50),       # 整数均匀分布[1,50)
    'weights': ['uniform', 'distance'],   # 分类选项
    'metric': ['euclidean', 'manhattan', 'minkowski'],
    'p': uniform(1, 3)                   # 连续均匀分布[1,4)
}

random_search = RandomizedSearchCV(
    KNeighborsRegressor(),
    param_distributions=param_dist,
    n_iter=100,           # 随机采样100组参数
    cv=5,                 # 5折交叉验证
    scoring='neg_mean_squared_error',
    n_jobs=-1,            # 使用所有CPU核心
    random_state=42       # 随机种子保证可复现
)

random_search.fit(X_train, y_train)
y_pred=random_search.predict(X_test)
# 评估模型
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"随机搜索模型评估")
print(f"均方误差（MSE）：{mse:.2f}")
print(f"R²分数：{r2:.2f}")
