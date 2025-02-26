import datetime

import requests
import bs4

# bilibili全站排行版
# 声明浏览器头文件,不写可能会被网站阻止访问,报418错误
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'}
# 声明要爬取的网页地址
url = "https://www.bilibili.com/v/popular/rank/all"
# 获取url的网页源码,并以上面浏览器头文件声明的方式(目的是伪装成浏览器)
res = requests.get(url, headers=head)
# 打印出状态码,并用状态码判断访问是否成功
# 200表示成功,400表示url错误,418表示被网站阻止访问(没有浏览器头文件)
stat = res.status_code
if stat == 200:
    print("访问成功,状态码:", stat,"开始作业")
    # 用bs4的html.parser的方式解析res.text
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # 找到所有div,class为c-single-text-ellipsis,可以去浏览器对应网页,按f12找
    # 这里的class_相当于h5的class
    targets = soup.find_all("div", class_="info")
    # 遍历,将结果打印出来
    ind = 1;
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    with open(f"bilibili全站排行榜{date}.csv", "w", encoding="utf-8",
              newline="") as f:
        f.write("名次,日期,视频名,up主,播放量,弹幕,url\n")
        for each in targets:
            inde = f"第{ind}名,"
            title = f"{each.a.text.strip()},"
            date2 = f"{date},"
            up = f"{each.span.text.strip()},"
            plays = f"{each.find('div', class_='detail-state').select('span')[0].text.strip()},"
            barrages = f"{each.find('div', class_='detail-state').select('span')[1].text.strip()},"
            movieUrl = f"http:{each.a.get('href')}\n"
            f.write(inde + date2 + title + up + plays + barrages + movieUrl)
            ind += 1
        print("成功")
else:
    print("爬取失败,状态码为:", stat)
