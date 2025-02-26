# 追加模式
import datetime

with open("newFile.txt", "a+", encoding="utf-8") as file:
    wrStr = "\n我是插入内容:"+datetime.datetime.now().strftime("%Y年%m月%d日%H:%M:%S")+"\n"
    file.write(wrStr)
    # 插入序列,需要手动换行
    file.writelines(["我是新数据1\n","我是新数据2\n"])
    #移动指针
    file.seek(0)

    # 读取文件一次性读取全部文件内容,速度较快,但文件过大时比较占用内存

    # valueall=file.read()
    # print("一次性读取文件\t",valueall)


    # 逐行读取文本文本
    # readline读取一行文本
    # 每调用一次读取一行
    # 参数size表示读取文件的字节数

    # print("第一行",file.readline())
    # print("第二行",file.readline())
    # print("第三行",file.readline())

    # readlines方法则是读取所有行，返回的是所有行组成的列表。

    lins=file.readlines()
    for i in lins:
        print(i)
