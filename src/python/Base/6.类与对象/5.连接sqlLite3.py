# 非关系形数据库 sqlLite3
import sqlite3

dbPath = "sql.db"
conn = sqlite3.connect(dbPath)
# 游标
cur = conn.cursor()
# 创建表
# createTable = "create table user(id int primary key,userName,password)"
# conn.execute(createTable);

# 插入记录
try:
    sql = "insert into user values(47,'admin','pwd1')"
    conn.execute(sql)
    conn.commit()
except:
    conn.rollback()
# 查询
sql = "select * from user"
cur.execute(sql)
print(cur.fetchall())
cur.close()
