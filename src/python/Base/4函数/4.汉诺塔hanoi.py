# 汉诺塔
step = 0


def hanoi(pic, x, y, z):
    global step
    step += 1
    print(step)
    if pic == 1:
        print(x, "==>", z)
    else:
        hanoi(pic - 1, x, z, y)
        print(x, "==>", z)
        hanoi(pic - 1, y, x, z)


print("汉诺塔小游戏")
pic = int(input("请输入汉诺塔的层数"))
hanoi(pic, "A", "B", "C")
