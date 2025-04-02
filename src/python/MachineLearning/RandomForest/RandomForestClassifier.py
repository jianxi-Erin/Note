
# 导入必要库
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import plot_tree
import seaborn as sns
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 或 ['Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 加载数据
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
class_names = iris.target_names

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 训练模型
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 预测评估
y_pred = clf.predict(X_test)
print("预测数据",y_pred)
print("真实数据",y_test)

print(f"准确率：{accuracy_score(y_test, y_pred):.2f}")

# 特征重要性可视化
plt.figure(figsize=(10, 6))
sns.barplot(x=clf.feature_importances_, y=feature_names)
plt.title("特征重要性")
plt.show()

# 混淆矩阵可视化
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=class_names, yticklabels=class_names)
plt.title("混淆矩阵")
plt.ylabel('真实标签')
plt.xlabel('预测标签')
plt.show()

# 可视化单个决策树
plt.figure(figsize=(20, 10))
plot_tree(clf.estimators_[0], 
          feature_names=feature_names,
          class_names=class_names,
          filled=True, 
          rounded=True,
          max_depth=2)  # 限制显示深度
plt.title("随机森林中的单个决策树（简化版）")
plt.show()