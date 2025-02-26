# 生成数据集
import pandas as pd
import numpy as np
import random

# 设置随机种子以保证结果可重复
np.random.seed(0)

# 定义数据量
num_samples = 500

# 设定系数（权重和偏置）
a = 0.1  # Age的系数
b = 1    # Income的系数
c = 0.5  # Credit Score的系数
d = 2000 # 偏置项
noise_sigma = 2000  # 噪声的标准差

# 生成数据
data = []
for _ in range(num_samples):
    age = random.randint(20, 60)  # 年龄在20到60之间
    income = random.randint(30000, 120000)  # 年收入在30k到120k之间
    credit_score = random.randint(300, 850)  # 信用评分在300到850之间
    
    # 计算贷款金额
    loan_amount = (a * age) + (b * income) + (c * credit_score) + d
    loan_amount += random.gauss(0, noise_sigma)  # 添加噪声
    
    data.append([age, income, credit_score, loan_amount])

# 转换为DataFrame
df = pd.DataFrame(data, columns=['Age', 'Income', 'Credit Score', 'Loan Amount'])

# 打印前5行
print(df.head())
# 输出
df.to_csv('loan_dataset.csv', index=False)