import random
import numpy as np

# 生成四行四列的数组,用零填充,类型为int型
block = np.zeros((4, 4), dtype='int')


def changeArr():
    """
        这个函数用于生成新的块
        原理:先获取所有的可使用坐标(遍历所有的块,选出块值为零的块的坐标)
        将这些块的坐标添加到可使用坐标中的列表
        在这些列表中随机选出一对坐标生成一个新块2或者4
    """
    addrList = []
    for row in range(4):
        for col in range(4):
            if not block[row, col]:
                addrList.append((row, col))
    addr = random.choice(addrList)
    # 随机获取一对坐标
    block[addr[0], addr[1]] = random.choice([2, 4])


def isOver():
    for row in range(4):
        for col in range(4):
            if block[row, col] == 0:
                return False
    for row in range(4):
        for col in range(3):
            if block[row, col] == block[row, col + 1]:
                return False
    for col in range(4):
        for row in range(3):
            if block[row, col] == block[row + 1, col]:
                return False
    return True


def isAbleToLeft():
    for row in range(4):
        for col in range(3, 0, -1):
            if block[row, col] != 0:
                i = 1
                while col - i >= 0:
                    if block[row, col - i] == 0:
                        return True
                    if block[row, col] == block[row, col - 1]:
                        return True
                    i += 1
    return False


def isAbleToRight():
    for row in range(4):
        for col in range(3):
            if block[row, col] != 0:
                i = 1
                while col + i <= 3:
                    if block[row, col + i] == 0:
                        return True
                    if block[row, col] == block[row, col + 1]:
                        return True
                    i += 1
    return False


def isAbleToUp():
    for col in range(4):
        for row in range(3, 0, -1):
            if block[row, col] != 0:
                i = 1
                while row - i >= 0:
                    if block[row - i, col] == 0:
                        return True
                    if block[row, col] == block[row - 1, col]:
                        return True
                    i += 1
    return False


def isAbleToDown():
    for col in range(4):
        for row in range(3):
            if block[row, col] != 0:
                i = 1
                while row + i <= 3:
                    if block[row + i, col] == 0:
                        return True
                    if block[row, col] == block[row + 1, col]:
                        return True
                    i += 1
                    # if arr[row,col]==arr[row,col-i]:
                    #      j=i-1
                    #      while j>=1:
                    #          if arr[row,col-j]==0:
                    #              return True
    return False


def toLeft():
    # 判断 合并
    for row in range(4):
        for col in range(0, 3):
            if block[row, col] == 0:
                continue
            else:
                i = 0
                while col + i < 3:
                    i += 1
                    if block[row, col + i] == 0:
                        continue
                    elif block[row, col + i] == block[row, col]:
                        block[row, col] += block[row, col + i]
                        block[row, col + i] = 0
                        break
                    else:
                        break
    # 判断 移动
    for row in range(4):
        for col in range(1, 4):
            i = 0
            while col - i - 1 >= 0:
                if block[row, col - 1 - i] == 0 and block[row, col - i] > 0:
                    block[row, col - 1 - i] = block[row, col - i]
                    block[row, col - i] = 0
                i += 1
    changeArr()
    play()


def toRight():
    for row in range(4):
        for col in range(3, 0, -1):
            if block[row, col] == 0:
                continue
            else:
                i = 0
                while col - i >= 0:
                    i += 1
                    if block[row, col - i] == 0:
                        continue
                    elif block[row, col - i] == block[row, col]:
                        block[row, col] += block[row, col - i]
                        block[row, col - i] = 0
                        break
                    else:
                        break
    for row in range(4):
        for col in range(2, -1, -1):
            i = 0
            while col + i + 1 <= 3:
                if block[row, col + 1 + i] == 0 and block[row, col + i] > 0:
                    block[row, col + 1 + i] = block[row, col + i]
                    block[row, col + i] = 0
                i += 1
    changeArr()
    play()


def toUp():
    for col in range(4):
        for row in range(0, 3):
            if block[row, col] == 0:
                continue
            else:
                i = 0
                while row + i < 3:
                    i += 1
                    if block[row + i, col] == 0:
                        continue
                    elif block[row + i, col] == block[row, col]:
                        block[row, col] += block[row + i, col]
                        block[row + i, col] = 0
                        break
                    else:
                        break
    # 判断 移动
    for col in range(4):
        for row in range(1, 4):
            i = 0
            while row - i - 1 >= 0:
                if block[row - 1 - i, col] == 0 and block[row - i, col] > 0:
                    block[row - 1 - i, col] = block[row - i, col]
                    block[row - i, col] = 0
                i += 1
    changeArr()
    play()


def toDown():
    for col in range(4):
        for row in range(3, 0, -1):
            if block[row, col] == 0:
                continue
            else:
                i = 0
                while row - i > 0:
                    i += 1
                    if block[row - i, col] == 0:
                        continue
                    elif block[row - i, col] == block[row, col]:
                        block[row, col] += block[row - i, col]
                        block[row - i, col] = 0
                        break
                    else:
                        break
    print(block)
    for col in range(4):
        for row in range(2, -1, -1):
            i = 0
            while row + i + 1 <= 3:
                if block[row + 1 + i, col] == 0 and block[row + i, col] > 0:
                    block[row + 1 + i, col] = block[row + i, col]
                    block[row + i, col] = 0
                i += 1
    changeArr()
    play()


def play():
    print(block)
    if isOver():
        print('game over')
    else:
        dir = input('请输入移动方向(l:左，r:右，u:上，d:下):')
        if dir not in ['l', 'r', 'u', 'd']: play()
        if dir == 'l':
            if isAbleToLeft():
                toLeft()
            else:
                play()
        if dir == 'r':
            if isAbleToRight():
                toRight()
            else:
                play()
        if dir == 'u':
            if isAbleToUp():
                toUp()
            else:
                play()
        if dir == 'd':
            if isAbleToDown():
                toDown()
            else:
                play()


changeArr()
play()
