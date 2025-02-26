import datetime

pro = {"方便面": 3.5, "火腿肠": 2, "面包": 1.5, "雪碧": 3, "农夫山泉": 2, "卤蛋": 1, "可口可乐": 3}
shoppingList = {};
print("欢迎光临")
print(pro)
while True:
    fl = False
    shop = input("你要买什么")
    if shop == "end":
        break
    else:
        if shop in pro.keys():
            fl = True
        else:
            print("您输入的商品不存在,请重新输入")
            fl = False
    if fl:
        inp = input("你要买几个:")

        shopCount = int(inp)

        if shop in shoppingList.keys():
            shoppingList[shop] += shopCount
        else:
            shoppingList[shop] = shopCount

sum = 0
no = 1;
print("id\t\t商品\t\t", "单价\t\t", "数量\t\t", "总价\t\t")

for i in shoppingList.keys():
    shang = i
    shu = shoppingList[i]
    danjia = float()
    danjia = pro.get(shang)
    zongjia = shu * danjia
    print(no, "\t\t", shang, "\t\t", shu, "\t\t", danjia, "\t\t", zongjia)
    sum += zongjia
    no += 1
print("你总共买了", no, "件产品")
print(f"应付{sum}元")
print("****************************")
pay = float(input("请付钱"))
if pay >= sum:
    yue = pay - sum
    print(f"您付了{pay},找你{yue}")
else:
    print("不够,打死你")
date = datetime.datetime.now()
# 原格式打印
print(date)
# 格式化日期
print(date.strftime("%Y年%m月%d日 %H:%M:%S"))
