import csv

with open("csvFile.csv", "r", encoding="utf-8", newline="") as file2:
    # 读取数据
    csvR=csv.reader(file2)
    for row in csvR:
        print(row)
    # DictReader以字典方式读取v
    csvRd = csv.DictReader(file2)
    for i in csvRd:
        print(i)
