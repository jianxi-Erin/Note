import requests
import bs4

# 批量下载图片,不清晰
# 声明浏览器头文件,不写可能会被网站阻止访问,报418错误
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}
url = "https://cn.bing.com/images/search?q=%E5%8E%9F%E7%A5%9E,go=%E6%90%9C%E7%B4%A2,qs=ds,form=QBIR,first=1,tsc=ImageHoverTitle"  # 需要爬取图片的网页地址
print(requests.get(url).status_code)
page = requests.get(url, headers=head)  # 得到网页源码
soup = bs4.BeautifulSoup(page.text, "html.parser")
# print(soup.prettify())
# 找到所有div,class为c-single-text-ellipsis,可以去浏览器对应网页,按f12找
# 这里的class_相当于h5的class
targets = soup.find_all("img", class_="mimg")
k = 1
for i in targets:
    href = f"{i.get('src')}"
    if href == "None":
        href = f"{i.get('data-src')}"
    print(i)
    print(k, href, len(href))
    # re = requests.get(href, headers=head)
    # sou = bs4.BeautifulSoup(re.text, "html.parser")
    # with open("w.html", "a", encoding="utf-8") as f:
    #     f.write(sou.text+"\n")
    # break
    # a = sou.find("div", class_="imgContainer")
    # print(a)
    # print(a.status_code)
    # f = open(f"img/{k}.jpg", 'wb')  # 以二进制格式写入img文件夹中
    # f.write(a.content)
    # f.close()
    # print(f"第{k}张图片下载完毕")
    # k += 1;
# 循环遍历下载图片
# num = 0
# for i in reg:
#     a = requests.get(i)

#     num = num+1
