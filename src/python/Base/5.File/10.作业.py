import csv

with open("csvFile.csv", "r", encoding="utf-8", newline="") as file2:
    # DictReader以字典方式读取v
    csvRd = csv.DictReader(file2)
    first = ""
    second = ""
    for i in csvRd:
        sex = i["性别"].strip()
        if sex == "男":
            first += f"{i}\n"
        elif sex == "女":
            second += f"{i}\n"
    # with open方式会自动关闭文件,不需要手动关闭
    with open("212.txt", "a", encoding="utf-8") as file:
        file.write(first)
        file.write(second)
