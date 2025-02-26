# 字典dict无序,可变,key唯一
# 字典定义
d = {"吕布": "口口布", "关羽": "关习习", "刘备": "刘baby"}
d1 = dict(num1=1, num2=2, num3=3)
print(d)
# 通过可以get获取value
print(d.get("吕布"))
print(d1["num1"])

# 添加元素或修改元素
d1['num4'] = 4
print(d1['num4'])

# 删除元素pop:
d1.pop("num4")
print(d1.keys())  # 显示可用的key值
# 获得所有的value
print(d1.values())
# 显示所有的键值对
print(d1.items())

# 更新多个值


d1.update(num1=2, num2=9)
print(d1.items())

d6 = {"张三": {"java": 90, "python": 89}, "张四": {"java": 79, "python": 84}, "张五": {"java": 45, "python": 57}}
print(d6.items())

d7 = {1: {"name": "张三", "age": 19}, 3: {"name": "王五", "age": 22},
      2: {"name": "赵六", "age": 18}}
print(sorted(d7.items()))
print(sorted(d7.items(),key=lambda b:b[1]["age"]))



