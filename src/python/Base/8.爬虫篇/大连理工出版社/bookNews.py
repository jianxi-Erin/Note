import bs4
import requests


def start(p):
    url = "http://sve.dutpbook.com/?_d=news,_f=news"
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
    }
    parm = {
        "p": p
    }
    get = requests.get(url, headers=head, params=parm)
    get.encoding = "utf-8"
    stat = get.reason
    print(stat)
    if stat == "OK":
        soup = bs4.BeautifulSoup(get.text, "html.parser")
        for i in soup.select("ul.newsList")[0].select("li"):
            href = "http://sve.dutpbook.com/" + i.select("a")[0]["href"]
            print(href)
            print(bs4.BeautifulSoup(requests.get(href, headers=head).text, "html.parser").select("div.newsDetail")[
                      0].text.strip())

        # 递归翻页
        pCount = int(soup.select("div.page")[0].select("a")[len(soup.select("div.page")[0].select("a"))-1].text)
        print("总页数",pCount)
        print("当前页数",p)
        p += 1
        if p > pCount:
            return 0
        else:
            start(p)


start(1)



