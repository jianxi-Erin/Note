# products = [("方便面", 3.5), ("火腿肠", 2), ("面包", 1.5), ("雪碧", 3), ("农夫山泉", 2), ("卤蛋", 1), ("可口可乐", 3)]
# print(products)
# sum = 0
# for i in range(len(products) - 1):
#     print("你要多少", products[i][0])
#     num = int(input())
#     sum += num * products[i][1]
# print("总收费", sum)
# print("=============================")
# products2 = [("方便面", 3.5), ("火腿肠", 2), ("面包", 1.5), ("雪碧", 3), ("农夫山泉", 2), ("卤蛋", 1), ("可口可乐", 3)]
# proname = ""
# projiage = ""
# while True:
#     proname = input("输入商品名")
#     if proname == "":
#         break;
#     projiage = float(input("输入商品价格"))
#     products2.append((proname, projiage))
# print(products2)
#
# print("=========================")
# # 执行字符串表达式
# print(eval("3/2"))
from appdirs import unicode

# 提取连续数字并相加,使用正则表达式\d数字
import re

str1 = 'sdfwe123fdasd78979a5dsdf457as465df3gdfg'
# \d数字
pattern = re.compile(r'\d+')
num = re.findall(pattern, str1)
num = [int(i) for i in num]
print(num)
su = 0
for i in num:
    su += i
print("结果", su)
# 判断两个字符串的公共子串,存在列表
str1 = "It's a nice day today"
str2 = "I'm very nice unhappy today"
strMax = str1 if len(str1) >= len(str2) else str2
strMin = str1 if len(str1) < len(str2) else str2

print("字符串1:",strMax," 长度为",len(strMax))
print("字符串2:",strMin," 长度为",len(strMin))

# print("字符串1:", str1)
# print("字符串2:", str2)
publicStrSet = set()
for i in range(len(strMin)):
    for j in range(i, len(strMin)):
        if strMax.count(strMin[i:j]) > 0:
            publicStrSet.add(strMin[i:j])
publicStr = list(publicStrSet)
print("两个字符串的公共子串有:", publicStr)
print("两个字符串的最大子串是:", max(publicStr))

# 学生信息管理
students = {}
ziduanList = []
print("学生管理系统")
while True:
    sno = input("请输入学生学号:")
    if sno == "":
        break
    elif sno in students:
        print("该学生已存在,请重新输入")
        continue
    name = input("请输入学生姓名:")
    gender = input("请输入学生性别:")
    age = int(input("请输入学生年龄:"))

    studentsList = []
    studentsList.extend([name, gender, age])
    ziduanList = ["name", "gender", "age"]
    students[sno] = dict(zip(ziduanList, studentsList))
print("原数据:")
print(students)
#     排序
print("排序后的样子:")
students = dict(sorted(students.items()))
print(students)
# 查询男生信息
print("性别为男生的数据:")
for i in students.keys():
    if students[i]["gender"] == "男":
        print(students[i])
# 删除学生姓名为空的学生
print("删除下面内容,名字为空:")
for i in list(students.keys()):
    if students[i]["name"] == "":
        print(students.pop(i))
# 性别为空的改为未知
print("若性别为空,则改为未知:")
for i in students.keys():
    if students[i]["gender"] == "":
        students[i]["gender"] = "未知"
print(students)
