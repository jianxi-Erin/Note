# 导入必要库
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 加载数据
housing = fetch_california_housing()
X = housing.data
y = housing.target
feature_names = housing.feature_names

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 训练模型
reg = RandomForestRegressor(n_estimators=100, random_state=42,n_jobs=-1)
reg.fit(X_train, y_train)

# 预测评估
y_pred = reg.predict(X_test)
print("预测数据",y_pred)
print("真实数据",y_test)
print(f"均方误差（MSE）：{mean_squared_error(y_test, y_pred):.2f}")
print(f"R²分数：{r2_score(y_test, y_pred):.2f}")

# 特征重要性可视化
plt.figure(figsize=(10, 6))
sns.barplot(x=reg.feature_importances_, y=feature_names)
plt.title("特征重要性")
plt.show()

# 实际值 vs 预测值可视化
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.3)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel('实际值')
plt.ylabel('预测值')
plt.title('实际值 vs 预测值')
plt.show()