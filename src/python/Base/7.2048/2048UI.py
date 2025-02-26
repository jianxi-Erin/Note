import random
import sys
import pygame as game

game.init()
# 声明成员变量颜色,字体颜色,字体,帧率,屏幕控制,屏幕,棋盘

bgColor = (250, 248, 239)
color1 = (187, 173, 160)
color2 = (205, 193, 180)
color3 = (238, 228, 218)
fontColor = (119, 110, 101)
bigTextFont = game.font.SysFont(None, 150)
normalTextFont = game.font.SysFont(None, 125)
smallTextFont = game.font.SysFont(None, 100)
FPS = 60
screenRect = None
screen = None
blockFather = game.Rect(50, 50, 500, 500)
# 存储所有的可放置坐标
locations = [[0] * 4 for i in range(4)]
# 存储所有存在的块数字
block = [[0] * 4 for i in range(4)]


def init():
    """
    初始化
    :return:
    """
    global bgColor, color1, color2, color3, fontColor, bigTextFont, FPS, screenRect, screen, blockFather, locations

    # 设置窗口标题宽高,获取尺寸对象
    game.display.set_caption("2048小游戏")
    screen = game.display.set_mode((850, 600))
    screenRect = screen.get_rect()
    screen.fill((250, 248, 239))
    # 设置棋盘
    blockFather = game.Rect(50, 50, 500, 500)
    # 初始化所有棋子的x,y位置
    for i in range(4):
        for j in range(4):
            locations[i][j] = [j * 120 + 90, i * 120 + 70]


def newBlock():
    """
    # 在空余位置生成新的块
    :return:
    """
    global block

    # 遍历所有可用的坐标
    location = []
    for x in range(4):
        for y in range(4):
            if block[x][y] == 0:
                location.append((x, y))
    # 随机产生一个坐标
    if location not in []:
        loc = random.sample(location, 1)[0]
        # 生成新块
        x = loc[0]
        y = loc[1]
        block[x][y] = 2
        print(f"在[{x}][{y}]生成新的块2")
        # 刷新棋盘
        for r in range(4):
            for c in range(4):
                print("", block[r][c], end="\t")
            print()
    else:
        game.quit()
        sys.exit()


def reDraw():
    """
    重绘对象
    :return:
    """
    global bgColor, color1, color2, color3, fontColor, bigTextFont, FPS, screenRect, blockFather
    # 绘制棋盘
    game.draw.rect(screen, color1, blockFather)
    screen.blit(bigTextFont.render(f"2048", True, fontColor), [575, 90])
    # screen.blit(smallTextFont.render(f"Step", True, fontColor), [575, 200])
    # screen.blit(smallTextFont.render(f"score", True, fontColor), [575, 300])

    # 一直绘制棋子
    for i in range(4):
        for j in range(4):
            # 绘制子棋盘
            game.draw.rect(screen, color2,
                           game.Rect(locations[i][j][0] - 20, locations[i][j][1], 100, 100))
            if block[i][j] != 0:
                # 绘制棋子底色
                g = game.Rect(locations[i][j][0] - 20, locations[i][j][1], 100, 100)
                game.draw.rect(screen, color3,
                               game.Rect(locations[i][j][0] - 20, locations[i][j][1], 100, 100))
                # 绘制棋子
                screen.blit(bigTextFont.render(f"{block[i][j]}", True, fontColor), locations[i][j])

    # 刷新界面
    game.display.update()


def blockMove(direction):
    global block, blockStep
    """
    # 块的移动接受控制命令,并且向对应的方向移动
    :param console:
    :return:
    """
    print(f"向{direction}方向移动")
    # 当所有元素无法移动或者循环时则退出循环,本次移动完成
    isMove = True
    # 保证所有元素移动并且一步到位
    while isMove:
        # 计数,用于统计有几个元素不能移动,当所有元素均不能移动时,退出循环
        moveCount = 0
        # 向上移动
        if direction == "w":

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
        elif direction == "a":
            for i in range(len(block)):
                for j in range(1, len(block[i])):
                    if block[i][j] != 0 and block[i][j - 1] in [0, block[i][j]]:
                        block[i][j - 1] += block[i][j]
                        block[i][j] = 0
                        break
                    else:
                        moveCount += 1
                    # 当本次棋盘无元素可以移动或合成,退出循环
                    isMove = False if moveCount >= 12 else True
        # 向下移动
        elif direction == "s":
            for i in range(len(block) - 1):
                for j in range(len(block[i])):
                    if block[i][j] != 0 and block[i + 1][j] in [0, block[i][j]]:
                        block[i + 1][j] += block[i][j]
                        block[i][j] = 0
                        break
                    else:
                        moveCount += 1
                    # 当本次棋盘无元素可以移动或合成,退出循环
                    isMove = False if moveCount >= 12 else True
                    # 向右移动
        elif direction == "d":
            for i in range(len(block)):
                for j in range(len(block[i]) - 1):
                    if block[i][j] != 0 and block[i][j + 1] in [0, block[i][j]]:
                        block[i][j + 1] += block[i][j]
                        block[i][j] = 0
                        break
                    else:
                        moveCount += 1
                    # 当本次棋盘无元素可以移动或合成,退出循环
                    isMove = False if moveCount >= 12 else True


def keyConsole():
    """
    监控按键并做出相应
    :return:
    """
    if event.key == game.K_RIGHT:
        # 控制向右移动
        blockMove("d")
    elif event.key == game.K_LEFT:
        # 向左移动
        blockMove("a")
    elif event.key == game.K_UP:
        # 向上移动
        blockMove("w")
    elif event.key == game.K_DOWN:
        # 向下移动
        blockMove("s")
    newBlock()


if __name__ == '__main__':
    init()
    newBlock()
    clock = game.time.Clock()
    run = True

    while run:
        # 设置刷新率
        clock.tick(FPS)
        # 监听鼠标和按键
        for event in game.event.get():
            # 点击退出按钮,则退出程序
            if event.type == game.QUIT:
                run = False
            elif event.type == game.KEYDOWN:
                keyConsole()
        reDraw()

    game.quit()
    sys.exit()
