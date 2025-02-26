import requests

print("下载中...")
url = "https://webstatic.mihoyo.com/upload/op-public/2020/09/27/fd431739ff26ceeb3010ac561d68446b_345688670889091949.mp4"  # 需要爬取图片的网页地址

page = requests.get(url)  # 得到网页源码
with open(f"movie/yuanshen.mp4", 'wb') as f:  # 以二进制格式写入img文件夹中
    f.write(page.content)
    f.close()
print(f"下载完毕")
