from sklearn.datasets import fetch_california_housing
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# 加载加州房价数据集
housing = fetch_california_housing()
X = housing.data  # 特征：经度、纬度、房龄等
y = housing.target  # 目标：房价中位数
feature_names = housing.feature_names

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建决策树回归器
reg = DecisionTreeRegressor(
    max_depth=4,  # 限制树深度
    criterion='squared_error'  # 分裂标准：均方误差
)
reg.fit(X_train, y_train)

# 计算MSE和R²分数
from sklearn.metrics import mean_squared_error, r2_score
y_pred = reg.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))

# 可视化特征重要性
importances = reg.feature_importances_
plt.barh(feature_names, importances)
plt.xlabel("Feature Importance")
plt.show()

from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [3, 4, 5, 6, 7, 8],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2']
}

grid_search = GridSearchCV(DecisionTreeRegressor(), param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Best cross-validation score:", -grid_search.best_score_)

# 使用最佳参数重新训练模型
best_reg = grid_search.best_estimator_
y_pred = best_reg.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))