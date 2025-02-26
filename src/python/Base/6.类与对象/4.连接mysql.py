# 关系型数据库 mysql

import pymysql


def selectAll(sql):
    global cursor
    # 执行sql语句
    cursor.execute(sql)

    # 获取单条数据
    # data = cursor.fetchone()

    # 获取受到影响的行数
    # row = cursor.rowcount()

    # 接受全部的返回结果行
    data1 = cursor.fetchall()
    for i in data1:
        for j in i:
            print(j, end="\t")
        print()
    # print(f"修改了{row}行")


def updata(sql):
    try:
        cursor.execute(sql)
        # 提交事务
        db.commit()
        print("成功")
    except:
        # 如果操作失败则回滚
        db.rollback()
        print("更新数据失败")


# 声明连接信息
db = pymysql.connect(host="localhost", user="root", password="zhangweiwei", database="xiaowei")
# 创建一个游标信息
cursor = db.cursor()

updata("delete from user where user='cctv'")
selectAll("select * from user")

# 关闭连接
db.close()
