'''
java : 声明变量要指定数据类型 int i  int i = 1；i= 0.1 不可以 数据类型报错
Javascript 声明变量可以不指定数据类型 vai i； var i=1；i= 0.1 可以
python 没有关键字，语法更简单，随意，定义及赋值
        不强制指定数据类型
        python是弱类型的语言（JavaScript也是）
'''
a=1
print(a)
b=0.1
print(b)
a=0.1
b="hello"
print(a,b)

'''
2.标识符命名规则    
    标识符;变量名 函数名 类名
    命名规则:见名知意
        标识符由字母 下划线和数字组成，且数字不能开头。
        python中的标识符是区分大小写的
        变量和函数:首字符小写
        类名:首字母大写
        可以用_连接，也可以用大小驼峰stu_name stuName
    标识符中不能使用关键字
'''

'''
3.python中的数据类型
 3.1 数值类型（数字类型）  “不同数值类型可以加减”
    3.1.1 整型(没有小数部分)  
    3.1.2 浮点型（有小数部分部分）
    3.1.3 布尔类型（数字类型的子类型）
    3.1.4 复数类型 complex 
 3.2 对象类型
    字符串，列表，元组，字典，集合
 3.3 其他特殊类型 None
'''
a=1
print(type(a))
b=1.0
print(type(b))
c=True
print(type(c))


    #复数类型
f=1+2j
print(f,type(f))
f1=1j
print(f1,type(f1))
f2=1+0j
print(f2,type(f2))
f3=1.1+2.1j
print(f3,type(f3))
print(f.real,f.imag) #获取复数的实部和虚部
# java int + str时 int隐式转换成str 然后做字符串拼接
# python没有隐式转换，

