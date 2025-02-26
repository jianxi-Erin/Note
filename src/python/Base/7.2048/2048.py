import random

# 初始化全局变量
block = None
blockStep = None


# 生成new块

def newBlock():
    """
    # 在空余位置生成新的块
    :return:
    """
    global block, blockStep

    # 遍历所有可用的坐标
    locations = []
    for x in range(len(block)):
        for y in range(len(block)):
            if block[x][y] == 0: locations.append((x, y))
    # 随机产生一个坐标
    if locations != []:
        location = random.sample(locations, 1)[0]
        # 生成新块
        block[location[0]][location[1]] = 2
        print(f"在[{location[0]}][{location[1]}]生成新的块2")
        # 刷新棋盘
        for r in range(len(block)):
            for c in range(len(block[r])):
                if block[r][c] == 0:
                    print("\t·", end="\t\t")
                else:
                    print("\t", block[r][c], end="\t\t")

            print(end="\n\n")
        print("===============================")
    else:
        gameOver()


def moveBlock(console):
    global block, blockStep
    """
    # 块的移动接受控制命令,并且向对应的方向移动
    :param console:
    :return:
    """
    # 当所有元素无法移动或者循环时则退出循环,本次移动完成
    isMove = True
    # 保证所有元素移动并且一步到位
    while isMove:
        # 计数,用于统计有几个元素不能移动,当所有元素均不能移动时,退出循环
        moveCount = 0
        # 向上移动
        if console == "w":

            # 遍历第一行的元素.因为向上移动.第0行不用移动
            # 将所有元素移合一行

            for i in range(1, len(block)):
                for j in range(len(block[i])):
                    if block[i][j] != 0 and block[i - 1][j] in [0, block[i][j]]:
                        block[i - 1][j] += block[i][j]
                        block[i][j] = 0
                    else:
                        moveCount += 1
                    # 当本次棋盘无元素可以移动或合成,退出循环
                    isMove = False if moveCount >= 12 else True
        # 向左移动
        elif console == "a":
            for i in range(len(block)):
                for j in range(1, len(block[i])):
                    if block[i][j] != 0 and block[i][j - 1] in [0, block[i][j]]:
                        block[i][j - 1] += block[i][j]
                        block[i][j] = 0
                    else:
                        moveCount += 1
                    # 当本次棋盘无元素可以移动或合成,退出循环
                    isMove = False if moveCount >= 12 else True
        # 向下移动
        elif console == "s":
            for i in range(len(block) - 1):
                for j in range(len(block[i])):
                    if block[i][j] != 0 and block[i + 1][j] in [0, block[i][j]]:
                        block[i + 1][j] += block[i][j]
                        block[i][j] = 0
                    else:
                        moveCount += 1
                    # 当本次棋盘无元素可以移动或合成,退出循环
                    isMove = False if moveCount >= 12 else True
                    # 向右移动
        elif console == "d":
            for i in range(len(block)):
                for j in range(len(block[i]) - 1):
                    if block[i][j] != 0 and block[i][j + 1] in [0, block[i][j]]:
                        block[i][j + 1] += block[i][j]
                        block[i][j] = 0
                    else:
                        moveCount += 1
                    # 当本次棋盘无元素可以移动或合成,退出循环
                    isMove = False if moveCount >= 12 else True


def control():
    global block, blockStep
    while True:
        # 判断控制命令,并调用对应的方法
        console = input("请输入控制命令(w上,a左,d右,s下):")
        if console in ["w", "s", "a", "d"]:
            print(f"向{console}方向移动", end="\t")
            # 步长递增
            blockStep += 1
            print("步长", blockStep)
            moveBlock(console)
            newBlock()
        #     判断游戏结束
        elif console == "end":
            gameOver()
            break
        else:
            print("命令错误,请重新输入")


def gameOver():
    """
    游戏结束,计算分数
    :return:
    """
    global block, blockStep
    maxBlock = max(max(block))
    score = maxBlock * 10 - blockStep
    print("游戏结束")
    print(f"您的分数:{score}")


def init():
    """
    #初始化
    :return:
    """
    global block, blockStep
    # 生成棋盘
    block = [[0] * 4 for i in range(4)]
    # 初始化步长
    blockStep = 0
    print("2048小游戏")
    print("初始化棋盘...")
    newBlock()


if __name__ == '__main__':
    init()
    control()
