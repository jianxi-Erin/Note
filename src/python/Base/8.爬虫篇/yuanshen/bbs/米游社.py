import requests
import bs4

url = "https://bbs.mihoyo.com/ys/"
head = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"
}
get = requests.get(url, headers=head)
get.encoding = "utf-8"
