#流程控制分支语句if
#help("keywords"),查看关键字
print("====打怪====")
HP=500
Hurt=int(input("本次攻击造成的伤害:"))
HP-=Hurt
if HP<=0 :
    print("Boss:gg,盒饭get")
    print("玩家胜利")
else:
     print("Boss:来呀,互相伤害呀")
print("===段位判断===")
experience=int(input("请输入经验值"))
if experience>=0 and experience<99 :
    print("镔铁")
elif experience<199:
    print("青铜")
elif experience<299:
    print("白银")
elif experience<399:
    print("黄金")
elif experience<499:
    print("钻石")
else:
     print("非法输入")
