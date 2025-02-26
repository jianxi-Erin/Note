import requests
import bs4

re = requests.get(" https://www.hnzj.edu.cn/info/1011/12554.htm")
re.encoding = "utf-8"
soup = bs4.BeautifulSoup(re.text, "html.parser")
with open("yuanma.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())
