import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns
# 设置 Matplotlib 使用支持中文的字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 1. 生成数据集
np.random.seed(42)
mean1 = [2, 3]
cov1 = [[1, 0.5], [0.5, 1]]
class1 = np.random.multivariate_normal(mean1, cov1, 100)

mean2 = [5, 6]
cov2 = [[1, -0.5], [-0.5, 1]]
class2 = np.random.multivariate_normal(mean2, cov2, 100)

X = np.vstack((class1, class2))
y = np.hstack((np.zeros(100), np.ones(100)))

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=57)

# 2. 定义sigmoid函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 3. 自定义逻辑回归类
class LogisticRegression:
    def __init__(self, learning_rate=0.01, n_iter=1000):
        self.lr = learning_rate
        self.n_iter = n_iter
        self.weights = None
        
    def fit(self, X, y):
        # 添加偏置项
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        m, n = X_b.shape
        self.weights = np.random.randn(n)
        
        for _ in range(self.n_iter):
            z = X_b.dot(self.weights)
            h = sigmoid(z)
            gradient = X_b.T.dot(h - y) / m
            self.weights -= self.lr * gradient
            
    def predict_proba(self, X):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        return sigmoid(X_b.dot(self.weights))
    
    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)

# 4. 训练模型
model = LogisticRegression(learning_rate=0.1, n_iter=1000)
model.fit(X_train, y_train)

# 5. 测试模型
y_pred = model.predict(X_test)
print(y_pred,y_test)
# 打印混淆矩阵
conf_matrix = confusion_matrix(y_test, y_pred)
print("混淆矩阵：\n", conf_matrix)

plt.figure(figsize=(8, 6))  # 设置图形大小
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=True,
            xticklabels=["0", "1"], yticklabels=["0", "1"])

# 添加标题和标签
plt.title("混淆矩阵", fontsize=16)
plt.xlabel("预测 Label", fontsize=14)
plt.ylabel("真实 Label", fontsize=14)

# 显示图形
plt.show()

accuracy = np.mean(y_pred == y_test)
print(f"测试集准确率: {accuracy:.2f}")

# 6. 可视化结果
plt.figure(figsize=(12,5))

# 训练数据分布
plt.subplot(1,2,1)
plt.scatter(class1[:,0], class1[:,1], c='blue', label='Class 0')
plt.scatter(class2[:,0], class2[:,1], c='red', label='Class 1')
plt.title("Training Data Distribution")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# 决策边界可视化
x1_min, x1_max = X[:,0].min()-1, X[:,0].max()+1
x2_min, x2_max = X[:,1].min()-1, X[:,1].max()+1
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max, 100),
                      np.linspace(x2_min, x2_max, 100))

Z = model.predict(np.c_[xx1.ravel(), xx2.ravel()])
Z = Z.reshape(xx1.shape)

plt.subplot(1,2,2)
plt.contourf(xx1, xx2, Z, alpha=0.4)
plt.scatter(X_test[:,0], X_test[:,1], c=y_test, edgecolors='k')
plt.title("Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()