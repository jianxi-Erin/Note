import csv
import re
from lxml import etree

import bs4
import requests

no = 1
url = "https://news.hnzj.edu.cn/hzyw.htm"
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}

print("start...")
with open("news.csv", "a", encoding="utf-8", newline="") as f:
    csvF = csv.writer(f)
    csvF.writerow(["no", "id", "url", "标题", "作者", "发布时间", "访问次数", "内容"])
    while True:
        if url == "":
            print("finish")
            break
        else:
            get = requests.get(url, headers=head)
            soup = bs4.BeautifulSoup(get.text, "html.parser")
            for itemUrl in soup.select("div.new-item.n"):
                try:
                    itemUrl = "https://news.hnzj.edu.cn/" + itemUrl.select("h3")[0].a["href"]
                    # itemUrl="https://news.hnzj.edu.cn/../info/1011/11666.htm"
                    itemValue = requests.get(itemUrl, headers=head)
                    itemValue.encoding = "utf-8"
                    # 解析页面
                    ht = etree.HTML(itemValue.text)
                    id = itemUrl[itemUrl.rfind("/") + 1:itemUrl.rfind("h") - 1]
                    title = ht.xpath("//h1//text()")[0]
                    tim = re.findall(r"(\d{4}-\d{2}-\d{2})", ht.xpath("//div[@align='center']/text()")[0])[0]
                    source = (ht.xpath("//div[@align='center']/text()")[0][
                              ht.xpath("//div[@align='center']/text()")[0].find("源") + 2:
                              ht.xpath("//div[@align='center']/text()")[
                                  0].find(
                                  "浏")] + "").strip()
                    pa = {
                        "clickid": id,
                        "owner": "1798158223",
                        "clicktype": "wbnews"}
                    times = requests.get(
                        "https://news.hnzj.edu.cn/system/resource/code/news/click/dynclicks.jsp",
                        params=pa).text.strip()
                    val = ht.xpath("//div[@class='v_news_content']//p//text()")
                    if val == "":
                        val = ht.xpath("//div[@class='v_news_content']//span//text()")

                    csvF.writerow([no, id, itemUrl, title, source, tim, times, val])
                    print(no, itemUrl, itemValue.reason,"             ",[no, id, itemUrl, title, source, tim, times, val])
                    no += 1
                except:
                    print(itemUrl,"爬取失败")
        try:
            # 获取下一页(因为下一页按钮第一页和其他下一页url不同)
            np = soup.select("span.p_next.p_fun")[0].a["href"]
            if np in ("hzyw/458.htm","hzyw/457.htm","hzyw/456.htm"):
                nextPage = "https://news.hnzj.edu.cn/" + np
            else:
                nextPage = "https://news.hnzj.edu.cn/hzyw/" + np
            print(get.reason + "\t\t\t\t\t\t\t\t\t下一页:" + nextPage)
            url = nextPage
        except:
            #如果爬取不到下一页,则停止
            url = ""
