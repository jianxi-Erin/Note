import bs4
import requests
import re

url = "http://sve.dutpbook.com/?_d=news,_f=newsDetail,id=8"
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
get = requests.get(url, headers=head)
get.encoding = "utf-8"
print(get.reason)
soup = bs4.BeautifulSoup(get.text, "html.parser")
va = soup.prettify()
print("标题:", soup.select("div.artHd")[0].h5.text)
body = soup.select("div.artEditor")[0].p.text.strip()
print("内容:", re.sub(r"\n+", "\n", body))
"""
打印结果
C:\Program Files\IDE\Python\Python310\python.exe" D:/Python/HelloPython/212/8.爬虫篇/大连理工出版社/book.py 
OK
标题: 我社倾情打造的护理专业系列教材，好评如潮
内容: 为适应我国高职高专护理教育的改革与发展、护理专业教学模式和课程体系改革的需要，依据以“人”为中心的护理理念，以知识、能力、素质综合发展和高等技术应用型护理人才的培养目标为导向，以高职高专护理职业技能的培养为根本，我社特邀请上海市海外名师、国家外国专家局科教文卫专家、上海思博职业技术学院卫生技术与护理学院院长沈小平总主编、组织来自全国各地30余所护理院校的资深教师及临床第一线的护理专家们倾力打造的高职高专护理系列规划教材项目于2012年启动，截至目前已出版教材近20种。本套教材面市后，深受用户欢迎，好评如潮，从发行数量及用户评价上都实现了突破性的进展。
本系列教材的特色:
 
1、坚持“三基五性”的编写原则，注重体现学科前沿
2、充分体现护理专业特色，适应职业能力培养要求
3、注重整套教材的整体优化，构建高职新型课程结构
4、配套立体化教学资源，下载方便，使用灵活，实时更新完善

进程已结束,退出代码0

"""