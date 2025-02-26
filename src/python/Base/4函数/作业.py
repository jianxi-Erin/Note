def sumScore(sid, name, *scores):
    sum = 0
    for i in scores:
        sum += i
    return sid, name, sum


def circular(r):
    return 3.1415926 * r * r, 2 * 3.1415926 * r


def rectangle(a, b):
    return a * b, (a + b) * 2


a = circular(3)
b = rectangle(3, 4)
print("圆形面积", a[0], "圆形周长", a[1])
print("矩形面积", b[0], "矩形周长", b[1])
# 使用自定义模块shape求周长面积:调用
import shape

area = shape.getArea(3, 4)
cir = shape.getPerimeter(3, 4)
print("矩形的面积是", area)
print("矩形的周长是", cir)
# 函数的作用域
# global函数内部修改全局变量
# nonlocal 内部函数修改外部函数
x = 3
def nec():
    global x
    x = 5
nec()
print(x)
def fir():
    y=4
    def sec():
        nonlocal y
        y=8
    sec()
    print(y)
fir()
