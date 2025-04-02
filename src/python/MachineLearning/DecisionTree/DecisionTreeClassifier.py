from sklearn.datasets import load_iris
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 加载数据
iris = load_iris()
X = iris.data  # 特征：萼片长宽、花瓣长宽
y = iris.target  # 目标：花的种类
feature_names = iris.feature_names
class_names = iris.target_names

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# 创建决策树分类器
clf = DecisionTreeClassifier(
    max_depth=3,  # 控制树的最大深度防止过拟合
    criterion='gini'  # 分裂标准：基尼系数
)
clf.fit(X_train, y_train)
y_pried=clf.predict(X_test)  # 预测测试集

# 评估准确率
print("混淆矩阵\n",confusion_matrix(y_test, y_pried))
print("分类报告",classification_report(y_test, y_pried))
# 可视化决策树
plot_tree(clf, 
          feature_names=feature_names, 
          class_names=list(class_names),
          filled=True,  # 填充颜色表示类别
          rounded=True)
plt.show()