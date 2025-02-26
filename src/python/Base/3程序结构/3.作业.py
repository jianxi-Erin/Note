# 遍历列表
import random

list = [45, 56, 12, 45, 78, 56, 12]
for i in list:
    print(i, end="\t")

# 2每个元素+10
# 第一种方法
list1 = [k + 10 for k in list]
print(list1, end="\n")
# 第二种方法
# for i in range(len(list)):
#     list[i]+=10
# print(list)

# i=0
# while i<len(list):
#     list[i]+=10
#     i+=1
# print(list)
# 3每个元素+10
list2 = [k + 10 for k in list]
print(list2, end="\n")
# 倒序输出
for i in reversed(range(10)):
    print(i)
for i in range(10, 0, -1):
    print(i)

# 剪刀石头布
# 1一局定胜负
# game = ["剪刀", "石头", "布"]
# player = game.index(input("请出剪刀,石头,布:"))
# computer = random.randint(0, 2);
# gamewin = [[0, 2], [1, 0], [2, 1]]
# print("玩家出", game[player])
# print("电脑出", game[computer])
# if player == computer:
#     print("平局")
# elif gamewin.count([player, computer]) != 0:
#     print("玩家赢")
# else:
#     print("玩家输了")

# 2.三局两胜
# game = ["剪刀", "石头", "布"]
# gamewin = [[0, 2], [1, 0], [2, 1]]
# resuleWin = 0
# resuleLose = 0
# while True:
#     if resuleWin == 2 or resuleLose == 2:
#
#         break
#     else:
#         player = game.index(input("请出剪刀,石头,布:"))
#         computer = random.randint(0, 2);
#         print("玩家出", game[player])
#         print("电脑出", game[computer])
#         if player == computer:
#             print("平局")
#         elif gamewin.count([player, computer]) != 0:
#             resuleWin += 1
#         else:
#             resuleLose += 1
# if resuleWin == 2:
#     print("玩家赢了")
# else:
#     print("玩家输了")


# 猜数字
# 一次机会
# com = random.randint(1, 100)
# num = int(input("猜数字,请输入一个数:"))
# if num == com:
#     print("你真棒,一猜就对")
# elif num > com:
#     print("不对哦,猜大了")
# elif num < com:
#     print("不对哦,猜小了")
# else:
#     print("你猜的范围好像不在线")
#直到猜对为止:
com = random.randint(1, 100)
min=1
max=100
while True:
    num = int(input("猜数字,请输入一个数:"))
    if num == com:
        print("你真棒,一猜就对")
        break
    elif num > com:
        max=num
        print("不对哦,猜大了,请输入",min,"到",max)
    elif num < com:
        min=num
        print("不对哦,猜小了,请输入",min,"到",max)
    else:
        print("你猜的范围好像不在线")


# #三次机会
for i in range(3):
    num = int(input("猜数字,请输入一个数:"))
    print("电脑生成的是",com)
    print("你猜的数字是",num)
    if num == com:
        print("你真棒,一猜就对")
        break
    elif num > com:
        max = num
        print("不对哦,猜大了,请输入", min, "到", max)
        print("还剩",2-i,"次机会")
    elif num < com:
        min = num
        print("不对哦,猜小了,请输入", min, "到", max)
        print("还剩",2-i,"次机会")
    else:
        print("你猜的范围好像不在线")


# 循环报数
# strs = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# con = 1
# ind = 0
# print(strs)
# while len(strs) != 1:
#     if con % 5 != 0:
#         print("队员", strs[ind], end="\t")
#     else:
#         print("淘汰", strs.pop(ind), end="\n")
#         ind -= 1
#     # print()
#     if ind >= len(strs) - 1:
#         ind = 0
#     else:
#         ind += 1
#     con += 1
# print("len(strs):", len(strs))
# print("con:", con)
# print("ind:", ind)
# print("===========================================")
# print("最后的组长", strs)
