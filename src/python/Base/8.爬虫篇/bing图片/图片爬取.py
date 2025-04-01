import requests
import bs4
import os

# 创建img文件夹
if not os.path.exists("img"):
    os.makedirs("img")

# 声明浏览器头文件
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}

url = "https://cn.bing.com/images/search?q=%E6%96%B9%E5%A4%A7%E5%90%8C&qft=+filterui:aspect-tall&form=IRFLTR&first=1&cw=1177&ch=723"  # 需要爬取图片的网页地址

# 获取网页内容
page = requests.get(url, headers=head)
soup = bs4.BeautifulSoup(page.text, "html.parser")

# 找到所有图片标签
targets = soup.find_all("img", class_="mimg")

# 下载图片
for k, i in enumerate(targets, start=1):
    href = i.get('src') or i.get('data-src')
    if not href:
        print(f"第{k}张图片URL未找到")
        continue

    try:
        # 下载图片
        response = requests.get(href, headers=head)
        if response.status_code == 200:
            # 保存图片
            with open(f"img/{k}.jpg", 'wb') as f:
                f.write(response.content)
            print(f"第{k}张图片下载完毕")
        else:
            print(f"第{k}张图片下载失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"第{k}张图片下载出错：{e}")