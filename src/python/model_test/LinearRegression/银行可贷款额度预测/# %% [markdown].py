# %% [markdown]
# 
# # 线性回归例子
# ## 银行贷款预测系统:通过贷款人的信息预测可贷款额度
# 

# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# %%
# 1. 读取数据
data = pd.read_csv("loan_dataset.csv")
print("数据预览：")
print(data.head())

# %%
# 2. 提取特征和目标变量
X = data[["Age","Income","Credit Score"]].values
y = data["Loan Amount"].values

# %%
# 3. 划分训练集和测试集
#  数据归一化（标准化）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# %%
# 4. 创建线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)  # 训练模型

# %%
# 5. 预测
y_pred_train = model.predict(X_train)  # 训练集预测
y_pred_test = model.predict(X_test)    # 测试集预测
print('训练集预测结果：', y_pred_train)
print('训练集实际结果：', y_train)
print('测试集预测结果：', y_pred_test)
print('测试集实际结果：', y_test)


# %%
# 6. 评估模型
mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)
r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)

print(f"训练集均方误差 (MSE): {mse_train}")
print(f"测试集均方误差 (MSE): {mse_test}")
print(f"训练集 R² 分数: {r2_train}")
print(f"测试集 R² 分数: {r2_test}")

# %%
# 7. 可视化结果
# 由于是多特征数据，我们选择一个特征（如年龄）进行可视化
import matplotlib.pyplot as plt
import matplotlib

# 设置全局字体为支持中文的字体
matplotlib.rcParams['font.family'] = 'SimHei'  # Windows 系统使用黑体
matplotlib.rcParams['font.size'] = 12  # 设置字体大小
matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号
plt.figure(figsize=(10, 6))
plt.scatter(data["Age"], data["Loan Amount"], color="blue", label="实际数据")
plt.plot(data["Age"], model.predict(X), color="red", linewidth=2, label="回归线")
plt.xlabel("Age")
plt.ylabel("Loan Amount)")
plt.title("线性回归拟合结果")
plt.legend()
plt.show()


