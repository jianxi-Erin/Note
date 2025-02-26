#变量
#**乘方
#/除精确
num1=5
num2=3
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)
print("===============")
#字符串也可以相加
#str*n,可以生成n个字符串
str1="维"
str2="晓"
print(str1+str2)
print(str1*6)
print("===============")
#int整形
#float浮点型
#str字符串形
#可以用type(变量名)查看所属类型
#直接int+str会报错,可以用强类型转换
print(type(num1))
print(type(str1))
print(str2+str1+str(num1)+str(num2)+"岁了")
#布尔型变量True False
b=True
print(b)
b=False
print(b)
#比较运算符两个==判断两边是否相等
print(57>23)
print(57<23)
print(27==27)
print(27!=27)
print("nice"=="nice")
print("nice"!="nice")
##and,or,not
print(True and True)
print(True and False)
print(False and True)


print(True or True)
print(True or False)
print(False or False)

print(not True)
print(not False)
