# bmi值
gradeBmis = []
gradeBmis.append(
    [(input("输入班级:"), input("输入姓名:"), float(input("输入身高(m):")), float(input("输入体重(kg):")))])
print(gradeBmis)
for i in gradeBmis:
    for k in i:
        print(k[0], k[1], k[2], k[3])
        grade, name, height, weight = k[0], k[1], k[2], k[3]
        bmi = weight / (height ** 2)
        bmi = ""
        if bmi < 18.5:
            bmi = "偏瘦"
        elif bmi < 25:
            bim = "正常"
        elif bmi < 30:
            bmi = "过重"
        else:
            bmi = "超重"
        print(grade, name, "的BMI值为", bmi, end="")

# 成绩判断
score = float(input("输入成绩:"))

if score > 90 and score <= 100:
    print("你的成绩优秀")
elif score > 80:
    print("你的成绩良好")
elif score > 70:
    print("你的成绩中等")
elif score > 60:
    print("你的成绩及格")
elif score < 60 and score >= 0:
    print("你的成绩不及格")
else:
    print("非法数据")
