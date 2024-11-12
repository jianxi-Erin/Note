list1 = [
    [7, 8, 7.5, 8.3, 8.2, 7.8],
    [8, 8.3, 8.5, 8.8, 8.2, 7.8],
    [9, 8, 7.5, 8.3, 8.2, 8.8],
    [6, 7, 7.5, 7.3, 7.2, 7.8],
    [8, 9, 9, 8.8, 9, 10]
]

def zf(scores):
    # 去掉最高分和最低分，计算平均分
    scores.remove(max(scores))
    scores.remove(min(scores))
    return round(sum(scores) / len(scores), 1)

# 输出选手的得分
for i, scores in enumerate(list1):
    print(f'第{i + 1}名选手的得分是：{zf(scores)}')
