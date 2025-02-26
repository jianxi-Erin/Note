import datetime, time


# 形参和实参可以需要一一对应
# 如果使用关键字参数可以使用参数名=值的形式忽略,必须用/分隔


#
# while True:
#     date = datetime.datetime.now()
#     # 原格式打印
#     print(date)
#     # 格式化日期
#     print(date.strftime("%Y年%m月%d日"))
#     # 格式化时间
#     print(date.strftime("%H:%M:%S"))
#     time.sleep(1)

def add(*args, **sh):
    a = sh["score"] = sum(args)
    return {sh["name"]: a}


def func(a, b, *args):
    return a, b, args


def jiecheng(num):
    if num == 1:
        return 1
    elif num >= 1:
        return num * jiecheng(num - 1)


def qie(n):
    n1 = 0
    n2 = 1

    return


def qie(n):
    if n in [0,1]:
        return 1
    else:
        return qie(n - 1) + qie(n - 2)


if __name__ == '__main__':
    # s = jiecheng(4)
    # print(s)
    s = qie(20)
    print(s)
