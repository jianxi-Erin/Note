# .csv以纯文本存储表格数据
# 导入csv模块
import csv

with open("csvFile.csv", "a", encoding="utf-8", newline="") as file:
    # 基于文件对象获取csv写入对象
    csvF = csv.writer(file)
    # 写入表头
    # csvF.writerow(["学号", "姓名", "性别", "年龄"])

    # 准备数据
    sno = input("请输入学生学号:")
    name = input("请输入学生姓名:")
    gender = input("请输入学生性别:")
    age = int(input("请输入学生年龄:"))
    studentsList = []
    studentsList.extend([sno, name, gender, age])
    # 写入一行数据
    csvF.writerow(studentsList)
