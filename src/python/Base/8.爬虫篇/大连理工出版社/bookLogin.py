import json
import requests

print("登录-post")
name = input("请输入用户名:")
pwd = input("请输入密码:")
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
# url路径
url = "http://sve.dutpbook.com/index.php?_d=login,_f=login,act=login"
search = {
    "userName": name,
    "userPwd": pwd
}
# params指定参数
re = requests.post(url, data=search, headers=head)
re.encoding = "utf-8-sig"
print("访问路径:", re.url)
print("连接状态:", re.reason)
# 将字符串类型转换为python对象类型
recode = json.loads(re.text)["code"]
if recode == 400:
    print("登录失败,账号或密码错误")
elif recode == 200:
    print("登陆成功")
