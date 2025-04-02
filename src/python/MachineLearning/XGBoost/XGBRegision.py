# XGB加州房价回归任务
import xgboost as xgb
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.datasets import fetch_california_housing

from sklearn.metrics import (
    mean_squared_error,  # MSE/RMSE
    mean_absolute_error,  # MAE
    mean_absolute_percentage_error,  # MAPE
    r2_score,  # R²
    explained_variance_score  # 解释方差
)

# 1.加载加州房价数据集（替代已废弃的波士顿房价数据集）
data = fetch_california_housing()
X, y = data.data, data.target

# 2.划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3.初始化 XGBoost 回归器
model = xgb.XGBRegressor(
    objective="reg:squarederror",  # 回归任务
    eval_metric="rmse",            # 评估指标
    random_state=42
)

# 4. 训练
model.fit(X_train, y_train)

# 5. 预测
y_pred = model.predict(X_test)

# 6. 评估
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
evs = explained_variance_score(y_test, y_pred)

# 打印结果
print("=== 任务评估指标 ===")
print(f"1. MSE (均方误差): {mse:.4f}")
print(f"2. RMSE (均方根误差): {rmse:.4f}")
print(f"3. MAE (平均绝对误差): {mae:.4f}")
print(f"4. MAPE (平均绝对百分比误差): {mape:.4%}")
print(f"5. R² (决定系数): {r2:.4f}")
print(f"6. Explained Variance Score (解释方差): {evs:.4f}")

# 7.超参数网格调优
param_grid = {
    "n_estimators": [100, 200, 300],
    "learning_rate": [0.01, 0.1, 0.2],
    "max_depth": [3, 4, 5],
    "subsample": [0.8, 1.0],
    "colsample_bytree": [0.8, 1.0],
}

# 使用GridSearchCV进行调优
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    scoring="neg_root_mean_squared_error",  # 使用RMSE作为评估指标
    cv=5,  # 5折交叉验证
    verbose=1,
    n_jobs=-1  # 使用所有CPU核心
)

grid_search.fit(X_train, y_train)

# 输出最佳参数
print(f"最佳参数: {grid_search.best_params_}")

# 使用最佳参数重新训练模型
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

# 重新预测和评估
y_pred = best_model.predict(X_test)

# 评估
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
evs = explained_variance_score(y_test, y_pred)

# 打印结果
print("=== 网格调优评估指标 ===")
print(f"1. MSE (均方误差): {mse:.4f}")
print(f"2. RMSE (均方根误差): {rmse:.4f}")
print(f"3. MAE (平均绝对误差): {mae:.4f}")
print(f"4. MAPE (平均绝对百分比误差): {mape:.4%}")
print(f"5. R² (决定系数): {r2:.4f}")
print(f"6. Explained Variance Score (解释方差): {evs:.4f}")


