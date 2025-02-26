import requests
import bs4


head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}


def getRequest(url, head):
    res = requests.get(url, headers=head)
    statCode = res.status_code
    if statCode == 200:
        # 解析网页
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        targets = soup.find("ul", class_="list-group listmain").find_all("li", class_="list-group-item")
        for i in targets:
            href = i.a.get("href")
            re = requests.get(href, headers=head)
            re.encoding = "utf-8"
            resoup = bs4.BeautifulSoup(re.text, "html.parser")
            reta = resoup.find("div", class_="artibody")
            for j in reta:
                with open("COVID-19-HENAN.txt", "a", encoding="utf-8") as f:
                    data = j.text.strip() + "\n"
                    f.write(data)
                    print(data)

    else:
        print("访问失败,错误码", statCode)


if __name__ == '__main__':
    for i in range(0,62):
        if i==0:
            url = "https://wsjkw.henan.gov.cn/ztzl/xxgzbdfyyqfk/yqtb/index.html"
        else:
            url = f"https://wsjkw.henan.gov.cn/ztzl/xxgzbdfyyqfk/yqtb/index_{i}.html"
        getRequest(url, head)
        print(i)
