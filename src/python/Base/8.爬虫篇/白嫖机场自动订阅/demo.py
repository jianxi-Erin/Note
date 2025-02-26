import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#白嫖机场自动订阅脚本
# 请修改用户名,密码,白嫖代码,以及订阅次数
user = "17637145793@163.com"
password = "weiwei5211314"
baipiaocode = "baipiao9356"
subscribt = 100


# 定义浏览器驱动位置
driver = webdriver.Chrome(service=Service(
    r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'))
print("登录中...")
driver.get("https://xn--mesv7f5toqlp.com/#/login")
time.sleep(3)
driver.find_elements(
    By.XPATH, "//input[contains(@type, 'text')]")[0].send_keys(user)
driver.find_elements(
    By.XPATH, "//input[contains(@type, 'password')]")[0].send_keys(password)
driver.find_element(By.XPATH, "//button[contains(., '登入')]").click()
time.sleep(3)
for i in range(0, subscribt):
    print(f"自动订阅中...[{i}]")
    driver.get("https://xn--mesv7f5toqlp.com/#/plan/1")
    time.sleep(3)
    driver.find_elements(
        By.XPATH, "//input[contains(@type, 'text')]")[0].send_keys(baipiaocode)  # 输入白嫖代码
    driver.find_element(By.XPATH, "//button[contains(., '验证')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[contains(., '下单')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[contains(., '结账')]").click()
    time.sleep(10)
print("订阅成功√")