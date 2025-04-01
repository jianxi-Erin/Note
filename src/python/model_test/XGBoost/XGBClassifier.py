# XGB鸢尾花分类任务
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix

# 1.加载鸢尾花数据集
iris = load_iris()
X, y = iris.data, iris.target

# 2.划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3.初始化 XGBoost 分类器
model = xgb.XGBClassifier(
    objective="multi:softmax",  # 多分类任务
    num_class=3,               # 类别数
    eval_metric="mlogloss",    # 评估指标
    random_state=42
)

# 4.训练
model.fit(X_train, y_train)

# 5.预测
y_pred = model.predict(X_test)

# 6.评估
print("Accuracy:", accuracy_score(y_test, y_pred))
print("混淆矩阵\n",confusion_matrix(y_test, y_pred))
print("分类报告",classification_report(y_test, y_pred))