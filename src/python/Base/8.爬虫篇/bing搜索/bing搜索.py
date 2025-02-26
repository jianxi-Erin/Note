import requests
import bs4


# 动态搜索bing
def init(searchStr):
    # 浏览器请求头
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
    }
    # url路径
    url = "https://cn.bing.com/search"
    search = {
        "q": searchStr,
        "first": "1",
        "FORM": "PERE"
    }
    # params指定参数
    re = requests.get(url, params=search, headers=head)
    re.encoding = "utf-8"
    print("访问路径:", re.url)
    # with open("bing.html", "w", encoding="utf-8") as f:
    #     f.write(re.text)
    # print(re.text)
    soup = bs4.BeautifulSoup(re.text, "html.parser")
    print(soup.prettify())
    aa = soup.find("ol", id="b_results")
    # print(aa)

    # for i in aa.children:
    #     print(i.select["div"])
    #     # print(i.a.get("href"))


if __name__ == '__main__':
    sear = input("必应_输入搜索内容:")
    init(sear)
