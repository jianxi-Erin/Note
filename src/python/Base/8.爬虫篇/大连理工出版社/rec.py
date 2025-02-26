import re
import requests

url = 'http://sve.dutpbook.com/?_d=textbook&_f=bookDetail&id=463'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/104.0.0.0 Safari/537.36'}

resp = requests.get(url, headers=headers)
result = resp.text

name = re.findall(r'<h1 class="name" id="btn_name">(.+)</h1>', result)
people = re.findall(r'<span id="btn_zz">(.+)</span>', result)
IBSN = re.findall(r'<p><label>ISBN：</label>(.+)</p>', result)
money = re.findall(r'<p class="price" id="btn_jq">(.+)</p>', result)
cbs = re.findall(r'<p><label>出版社：</label>(.+)</p>', result)
time = re.findall(r'<p><label>出版时间：</label>(.+)</p>', result)
print(name)
print(people)
print(IBSN)
print(money)
print(cbs)
print(time)
