import urllib.request  # 导入urllib的请求模块request

import bs4
from lxml import etree

url = "http://sve.dutpbook.com/?_d=news&_f=news&p=2"
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}
no = 1

response = urllib.request.urlopen(url)  # 调用urllib.request库的urlopen()方法打开网址
html = response.read().decode("utf-8")  # 使用read()方法读取爬到的内容，并以utf-8方式编码
print(response.status)  # 打印响应的状态码
ht = etree.HTML(html)

for i in range(4):
    url = "http://sve.dutpbook.com/" + ht.xpath('//li[@class="pic"]//a[@class="tit f-toe"]/@href')[i]
    title = ht.xpath('//li[@class="pic"]//a[@class="tit f-toe"]//text()')[i]
    date = ht.xpath('//li[@class="pic"]//p[@class="date"]/text()')[i]
    re = {"no": no, "title": title, "date": date, "url": url}
    print(re)
    no += 1

# soup = bs4.BeautifulSoup(html, "html.parser")
# li = soup.select("li.pic")
# for i in li:
#     title = i.select("a.tit")[0].text
#     u = "http://sve.dutpbook.com/" + i.select("a.tit")[0]["href"]
#     date = i.select("p.date")[0].text
#     re = {"no": no, "title": title, "date": date, "url": u}
#     print(re)
#     no += 1