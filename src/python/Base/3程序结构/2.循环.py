# for 迭代对象 in 可迭代对象
# range(m,n,x)产生m到n的序列,步长为x
print("=========乘法口诀表=============")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "*", i, "=", i * j, end="\t")
    print()
else:
    print("最先执行我")
print("===================")
i = 1
while i < 6:
    print(i, end="\t")
    i += 1
else:
    print("最先执行我")

# 输入学名字
print("==================")
name = []
while True:
    na = input("输入姓名")
    if na == "end":
        break;
    name.append(na)
print(name)
# for循环
# for i in range(5):
#     name.append(input("输入姓名"))
# print(name)

