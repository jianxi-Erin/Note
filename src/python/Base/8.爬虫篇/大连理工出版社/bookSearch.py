import csv
import bs4
import requests
import re
import sqlite3


def insert(values):
    dbPath = "books.db"
    conn = sqlite3.connect(dbPath)
    # 游标
    cur = conn.cursor()
    # 创建表
    # createTable = "create table book(书名,作者,ISBN,出版社,出版时间,价格,图片,url)"
    # conn.execute(createTable)

    # 插入记录
    try:
        sql = "insert into book values(?,?,?,?,?,?,?,?)"
        conn.execute(sql, values)
        conn.commit()
    except:
        print("写入数据失败")
        conn.rollback()


def downLoad(i):
    search["p"] = i
    reso = bs4.BeautifulSoup(requests.get(url, params=search, headers=head).text, "html.parser")

    r = reso.find("ul", class_="searchList").find_all("li")
    for i in r:
        href = "http://sve.dutpbook.com/index.php" + i.a["href"]
        bookValue = bs4.BeautifulSoup(requests.get(href, headers=head).text, "html.parser").find("div",
                                                                                                 class_="clmMain f-fl")
        bookName = bookValue.select("h1.name")[0].text.strip()
        pic = "http://sve.dutpbook.com/" + bookValue.select("div.bookPic")[0].img["src"]
        infolist = re.split("\\n|：", bookValue.select("div.info")[0].text.strip())
        infokey = [infolist[i] for i in range(len(infolist)) if i % 2 == 0]
        infovalue = [infolist[i] for i in range(len(infolist)) if i % 2 == 1]
        info = dict(zip(infokey, infovalue))
        price = bookValue.select("p.price")[0].text.strip()
        insert((bookName, info['作者'], info['ISBN'], info['出版社'], info['出版时间'], price, pic, href))


# 输入参数

print("搜索-get传参")
searchType = input("请输入检索类型(0:书名,1:书号,2:作者,4:全部):")
# 判读输入的类型是否为有效值
if "0124".count(searchType) == 0:
    searchType = 4
searchName = input("请输入检索内容")
# 定义浏览器头文件
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
# 定义url路径
url = "http://sve.dutpbook.com?"
# 定义搜索参数
search = {
    "_d": "textbook",
    "_f": "searchBook",
    "keyword": searchName,
    "type": searchType,
    "p": "1"
}

# 开始访问
res = requests.get(url, params=search, headers=head)
# 设置编码
res.encoding = "utf-8"

# 打印访问路径和状态
print("访问路径:", res.url)
print("连接状态:", res.reason)
# 使用Beautifulsoup解析网站
soup = bs4.BeautifulSoup(res.text, "html.parser")
# 判断是否多页
page = soup.find("div", class_="page")
if page is not None:
    print("搜索内容:多页")
    # 使用正则表达式获取末页
    try:
        # 有末页按钮的情况
        pageCount = re.findall("\d+", page.select("a.bt")[2]["href"])[1]
        print("总页数为:", pageCount)
        for i in range(1, int(pageCount) + 1):
            print("下载中", "." * i, "\t\t\t\t\t", int(i / int(pageCount) * 100), "%")
            downLoad(i)
        print("finish")
    except:
        # 没有末页按钮的清空
        pageCount = page.select("a")[len(page.select("a")) - 1].text
        print("总页数为:", pageCount)
        for i in range(1, int(pageCount) + 1):
            print("下载中", "." * i, "\t\t\t\t\t", int(i / int(pageCount) * 100), "%")
            downLoad(i)
        print("finish")
else:
    print("搜索内容:单页")
    print("下载中", "...""\t\t\t\t\t", "0%")
    downLoad(1)
    print("下载中", "...""\t\t\t\t\t", "100%")
    print("finish")
