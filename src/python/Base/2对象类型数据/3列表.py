# 列表的定义
list1 = [1, 'a', True, 1.3]
list2 = [1, 'a', True, 1.3, (1, 'a', True), [1, 'a', True]]
print(list1)
print(list2)
print(type(list1))

print(type(list2))

# list构造函数
# 等号后面要是可迭代的iterable

list3 = list("1233242345")
print(list3)

# 列表元素访问
# 正序索引
# 逆序索引
# 切片
print(list3)
a = list3[0]
print(a)

# 3列表元素的增删改
# list1[index]=value
# list[::]=()切片给多个元素赋值,value必须是可迭代类型的
list1[0] = '000'
print(list1)
list1[1:] = 1, 2, 3
print(list1)

# 增加列表元素
# 列表a+=列表b
print(list1)
list1 += list2
list1 *= 2

# 内置方法
# append(value)追加元素,可以追加元素/元组/列表.保留原格式
# extends(value)追加元素,全部转换为元素
# insert(index,value)在指定位置添加元素(元素/元组/列表)
list5 = ["a", "b", "c"]
print(list5)
list5.insert(1, "我在这里")
print(list5)

# 删除元素
# remove(value)删除第一个和指定值相同的值,如果该元素不存在则会保报错
# pop(index)删除指定索引的值,默认删除最后一个元素
# del list[],删除指定索引范围的元素
del list5[1:2]

# 查找元素
# list.index(value,start,end)查找value在list的出现位置,也可以指定start和end ,如果查不到则报错
# list.count(value)查找value在list出现的次数,若不存在则返回0

# 列表推导式
block = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
k = [block[i][i] for i in range(len(block))]
c = [block[i][len(block) - i - 1] for i in range(len(block))]
print("列表:", block);
print("对角线", k, end="\n");
print("反对角线", c, end="\n");
# 对应拼接
name = ["张三", "李四", "王五", "赵六"]
course = ["python", "java"]
scoure = [80, 54, 76, 89, 100, 80, 60, 50]
nameCourse = [(i, j) for i in name for j in course]

k = 0
nameCourseScore = []

for i in range(len(name)):
    for j in range(len(course)):
        nameCourseScore.append((name[i], course[j], scoure[2 * i + j]))

# 计算总分
nameSum = [(nameCourseScore[i][0], nameCourseScore[i][2] + nameCourseScore[i][2]) for i in range(len(nameCourseScore))]
print(nameCourseScore)
print(nameSum)

# a = [0, 1]
# for i in range(2, 22):
#     a.append(a[i - 1] + a[i - 2])
# print(a)
