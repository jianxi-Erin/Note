# Boss直聘数据爬取,使用selenium模块
import csv
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 定义浏览器驱动位置
driver = webdriver.Chrome(service=Service(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'))
# 设置最长等待时间
driver.implicitly_wait(15)


def login():
    '''
    此方法用于boos直聘登录
    :return: 登陆后的cookie,用于保持登陆状态
    '''

    # 访问登录页面
    driver.get("https://www.zhipin.com/user/login.html")

    # 延时20秒返回cookie
    print("请用手机扫码登录,20秒后自动开始爬取数据")
    time.sleep(20)
    return driver.get_cookies()[0]


def work(myCookie):
    """
    爬取数据
    :return:
    """
    # 定义url
    url = "https://www.zhipin.com/web/geek/job"
    # 定义字段序号
    id = 1
    # 定义查询专业
    major = "人工智能"
    # 定义城市列表["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉", "西安", "郑州"]
    cityList = {"101010100": "北京", "101020100": "上海", "101280100": "广州", "101280600": "深圳", "101210100": "杭州",
                "101270100": "成都", "101200100": "武汉", "101110100": "西安",
                "101180100": "郑州"}
    # 定义学历为大专,202为内部编码,通过分析都得到
    degree = "202"
    # 定义参数
    param = {
        "query": major,
        "city": "",
        "degree": "202",
        "page": "1"
    }
    # 定义cookie
    cookie = {
        'domain': myCookie.get("domain"),
        'name': myCookie.get('name'),
        'value': myCookie.get('value'),
        "expires": myCookie.get('expiry'),
        'path': myCookie.get('path'),
        'Secure': myCookie.get('secure')
    }

    with open("boss.csv", "a", newline="", encoding="utf-8") as f:
        csvF = csv.writer(f)
        csvF.writerow(["序号", "岗位", "工作地域", "薪资待遇", "任职要求"])
        # 遍历城市列表
        for city in cityList.keys():
            param["city"] = city
            # 获取末页
            driver.get(requests.get(url, params=param).url)
            last = int(driver.find_element(By.XPATH, '//div[@class="pagination-area"]//a[last()-1]').text + "")
            # 遍历所有页
            for p in range(1, last + 1):
                param["page"] = p
                if p != 1:
                    # 参数拼接并访问
                    driver.add_cookie(cookie)
                    # 使用requests帮忙拼接参数作为浏览器的url
                    driver.get(requests.get(url, params=param).url)

                time.sleep(2)

                for li in driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li'):
                    vdata = []
                    # 序号
                    vdata.append(id)
                    # 工作名称
                    vdata.append(li.find_element(By.XPATH, './div[1]/a/div[1]/span[1]').text)
                    # 工作地域

                    vdata.append(li.find_element(By.XPATH, './div[1]/a/div[1]/span[2]/span').text)
                    # 薪资待遇
                    vdata.append(li.find_element(By.XPATH, './div[1]/a/div[2]/span[1]').text)
                    # 任职要求
                    vdata.append(li.find_element(By.XPATH, './div[1]/a/div[2]/ul').text.replace("\n", ","))
                    csvF.writerow(vdata)
                    print(vdata)
                    id += 1

                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", cityList[city], "第", p, "页/共", last, "页", "爬取中",
                      "." * p)


if __name__ == '__main__':
    # 获取cookie

    print("start")
    cook = login()
    work(cook)
    print("finish")
