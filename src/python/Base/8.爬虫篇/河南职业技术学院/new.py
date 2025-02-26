import bs4
import requests
from lxml import etree
import re

url = "https://news.hnzj.edu.cn/info/1011/11833.htm"
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
get = requests.get(url, headers=head)
get.encoding = "utf-8"
print(get.reason)
#使用XPATH写入字符文件
ht = etree.HTML(get.text)
title = ht.xpath("//h1/text()")[0]

tim = re.findall(r"(\d{4}-\d{2}-\d{2})", ht.xpath("//div[@align='center']/text()")[0])[0]
source = (ht.xpath("//div[@align='center']/text()")[0][
         ht.xpath("//div[@align='center']/text()")[0].find("源") + 2:ht.xpath("//div[@align='center']/text()")[0].find(
             "浏")]+"").strip()
pa = {
    "clickid": url[35:-4],
    "owner": "1798158223",
    "clicktype": "wbnews"}
times = requests.get(
    "https://news.hnzj.edu.cn/system/resource/code/news/click/dynclicks.jsp", params=pa).text.strip()
val = ht.xpath("//div[@class='v_news_content']/p/text()")
fileName = url[35:-4] + ".txt"
with open(fileName, "a", encoding="utf-8") as f:
    f.write("url:" + url + "\n")
    f.write("新闻标题:" + title + "\n")
    f.write("发布时间:" + tim + "\n")
    f.write("来源:" + source + "\n")
    f.write("浏览次数:" + times + "\n")
    f.write("内容:" + "\n")
    for i in val:
        f.write(i+"\n")
#使用bs4爬取图片
soup=bs4.BeautifulSoup(get.text,"html.parser")
for i in soup.select("div#vsb_content_2")[0].select("img"):
    imgUrl="https://news.hnzj.edu.cn/"+i["src"]
    imgName=imgUrl[imgUrl.rfind("/")+1:]
    with open(imgName,"wb",encoding="utf-8") as im:
        imgData=requests.get(imgUrl).content
        im.write(imgData)
print("finish")
