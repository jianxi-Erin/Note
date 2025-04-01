import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib
# 设置 Matplotlib 使用支持中文的字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 1. 读取数据
data = {
    '编号': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    '色泽': ['青绿', '乌黑', '乌黑', '青绿', '浅白', '青绿', '乌黑', '乌黑', '乌黑', '青绿', '浅白', '浅白', '青绿', '浅白', '乌黑', '浅白', '青绿'],
    '根蒂': ['蜷缩', '蜷缩', '蜷缩', '蜷缩', '蜷缩', '稍蜷', '稍蜷', '稍蜷', '稍蜷', '硬挺', '硬挺', '蜷缩', '稍蜷', '稍蜷', '稍蜷', '蜷缩', '蜷缩'],
    '敲声': ['浊响', '沉闷', '浊响', '沉闷', '浊响', '浊响', '浊响', '浊响', '沉闷', '清脆', '清脆', '浊响', '浊响', '沉闷', '浊响', '浊响', '沉闷'],
    '纹理': ['清晰', '清晰', '清晰', '清晰', '清晰', '清晰', '稍糊', '清晰', '稍糊', '清晰', '模糊', '模糊', '稍糊', '稍糊', '清晰', '模糊', '稍糊'],
    '脐部': ['凹陷', '凹陷', '凹陷', '凹陷', '凹陷', '稍凹', '稍凹', '稍凹', '稍凹', '平坦', '平坦', '平坦', '凹陷', '凹陷', '稍凹', '平坦', '稍凹'],
    '触感': ['硬滑', '硬滑', '硬滑', '硬滑', '硬滑', '软粘', '软粘', '硬滑', '硬滑', '软粘', '硬滑', '软粘', '硬滑', '硬滑', '软粘', '硬滑', '硬滑'],
    '好瓜': ['是', '是', '是', '是', '是', '是', '是', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否']
}
df = pd.DataFrame(data)

# 2. 数据编码
label_encoders = {}
for column in df.columns[1:-1]:  # 对特征进行 LabelEncoder
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

df['好瓜'] = df['好瓜'].map({'是': 1, '否': 0})  # 二值化目标变量

# 3. 增加交叉特征
df['色泽_敲声'] = df['色泽'] * df['敲声']

# 4. 特征与标签划分
X = df.iloc[:, 1:-1]
y = df['好瓜']
# X = np.array([[1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0],
#               [1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 1, 1], [1, 2, 2, 0, 2, 1],
#               [2, 1, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [2, 0, 0, 2, 2, 0],
#               [1, 0, 1, 1, 1, 0], [1, 0, 1, 0, 0, 0], [2, 0, 0, 0, 0, 0],
#               [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [2, 2, 2, 2, 2, 0],
#               [2, 0, 0, 2, 2, 1], [1, 1, 0, 1, 0, 0]])
# y = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0])
# 5. 数据集划分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)


# 6. 标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 7. 逻辑回归模型（优化）
model = LogisticRegression(penalty='l1', solver='liblinear', C=1.0, max_iter=5000, class_weight='balanced')

model.fit(X_train, y_train)

# 8. 预测
y_pred = model.predict(X_test)

# 9. 评估
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print("优化后的混淆矩阵：\n", conf_matrix)

print(f"优化后的模型准确率：{accuracy:.2f}")

plt.figure(figsize=(8, 6))  # 设置图形大小
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=True,
            xticklabels=["0", "1"], yticklabels=["0", "1"])

# 添加标题和标签
plt.title("混淆矩阵", fontsize=16)
plt.xlabel("预测 Label", fontsize=14)
plt.ylabel("真实 Label", fontsize=14)

# 显示图形
plt.show()