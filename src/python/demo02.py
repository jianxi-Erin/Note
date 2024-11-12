import math

def fun(x, n):
    # 初始化多项式和为 1（即 s = 1）
    s = 1
    # 逐项累加多项式的值
    for i in range(1, n + 1):
        s += x**i / math.factorial(i)
    return s

# 测试代码
x = float(input("请输入 x 的值："))
n = int(input("请输入 n 的值："))
result = fun(x, n)
print(f'多项式计算结果为：{result:.4f}')