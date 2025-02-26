# 导入必要的库
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 加载乳腺癌数据集（二分类问题，良/恶性肿瘤）
data = load_breast_cancer()
X = data.data  # 特征矩阵s
y = data.target  # 目标变量（0=恶性，1=良性）

# 划分训练集和测试集（80%训练，20%测试）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 标准化数据（逻辑回归对特征尺度敏感）
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 创建逻辑回归模型并训练
model = LogisticRegression(max_iter=1000)  # 增加迭代次数确保收敛
model.fit(X_train, y_train)

# 预测测试集结果
y_pred = model.predict(X_test)

# 评估模型性能
print("准确率:", accuracy_score(y_test, y_pred))
print("\n混淆矩阵:\n", confusion_matrix(y_test, y_pred))
print("\n分类报告:\n", classification_report(y_test, y_pred))

# 查看单个样本的预测概率（输出属于0类和1类的概率）
sample_idx = 0
print(f"\n样本 {sample_idx} 的预测概率:", model.predict_proba([X_test[sample_idx]]))