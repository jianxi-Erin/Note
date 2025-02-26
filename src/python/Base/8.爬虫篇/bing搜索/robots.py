import requests
url = "https://www.bing.com/robots.txt"
re = requests.get(url)
print(re.text)
