import requests
import bs4

url = "http://sve.dutpbook.com/robots.txt"
get = requests.get(url)
get.encoding = "utf-8"
print("访问状态:", get.reason)
if get.reason == "OK":
    print(get.text)
else:
    print("允许爬取")

