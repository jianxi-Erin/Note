#字典与查询
#字典={key:value,key:value,key:value}
score={"李小名":67,"张太丰":78,"太丰":92,"张丰":89,"小丰":98,"陈丰":89}
print("========成绩查询系统========")
name=input("请输入名字:")
print(name+"的成绩为"+str(score[name]))
