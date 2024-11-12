import math

def fun(x, y):
    # 计算斜边的长度
    return math.sqrt(x**2 + y**2)

# 输入两个直角边的长度
leg1, leg2 = eval(input('输入两条直角边，以逗号分隔：'))
# 输出计算结果，保留两位小数
print('斜边的长度为：{:.2f}'.format(fun(leg1, leg2)))
