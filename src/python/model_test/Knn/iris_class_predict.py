# 使用knn算法解决鸢尾花分类问题
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# 加载Iris数据集
iris = load_iris()
# print("Iris数据集的描述:", iris.DESCR)
X = iris.data  # 特征
y = iris.target  # 标签

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 标准化特征
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 创建KNN分类器，设置K=3
knn = KNeighborsClassifier(n_neighbors=3)

# 训练模型
knn.fit(X_train, y_train)

# 使用测试集进行预测
y_pred = knn.predict(X_test)

# 计算准确率
report = classification_report(y_test, y_pred)
print(f"分类报告: {report}")