import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
data = pd.read_csv("credit_dataset.csv")
print(data.head())

# 特征和目标变量
X = data[['CreditScore', 'Income', 'Age', 'Debt']]
y = data['Default']

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

from imblearn.over_sampling import SMOTE

# 应用 SMOTE 过采样
smote = SMOTE(sampling_strategy='auto', random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# 打印过采样后的数据分布
print(y_train.value_counts())

# 训练逻辑回归模型
model = LogisticRegression()
# 使用class_weight='balanced'(设置权重)参数来处理类别不平衡问题
model = LogisticRegression(class_weight = {0: 1, 1: 1.05})
model.fit(X_train, y_train)

# 预测与评估
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率: {accuracy:.2f}")

# 混淆矩阵
conf_matrix = confusion_matrix(y_test, y_pred)
print("混淆矩阵：")
print(conf_matrix)

# 分类报告
print("分类报告：")
print(classification_report(y_test, y_pred))

# 可视化混淆矩阵
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Not Default', 'Default'], 
            yticklabels=['Not Default', 'Default'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

