import pandas as pd
import numpy as np

# 设置随机种子以确保结果可重复
np.random.seed(42)

# 数据集大小
n_samples = 1000

# 生成虚拟数据
CreditScore = np.random.randint(300, 850, n_samples)  # 信用评分范围 300-850
Income = np.random.normal(50000, 15000, n_samples).astype(int)  # 年收入，平均 50000，标准差 15000
Age = np.random.normal(40, 10, n_samples).astype(int)  # 年龄，平均 40，标准差 10
Debt = np.random.normal(10000, 5000, n_samples).astype(int)  # 债务水平，平均 10000，标准差 5000

# 计算违约概率（简化模型）
# 违约概率与信用评分、收入、年龄和债务有关
# 这里使用一个简单的线性组合来生成违约概率
logit = (
    -6 + 0.005 * CreditScore - 0.00001 * Income + 0.01 * Age + 0.0001 * Debt
)
prob = 1 / (1 + np.exp(-logit))  # 使用 Sigmoid 函数得到违约概率

# 根据违约概率生成是否违约（0 表示未违约，1 表示违约）
Default = np.random.binomial(1, prob)

# 创建数据框
data = pd.DataFrame({
    'CreditScore': CreditScore,
    'Income': Income,
    'Age': Age,
    'Debt': Debt,
    'Default': Default
})

# 保存数据集到 CSV 文件
data.to_csv('credit_dataset.csv', index=False)