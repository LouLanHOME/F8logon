import os
import time
import base64
import ddddocr
from selenium import webdriver

cd = os.getcwd()
with open("Config.txt", 'r') as f:
    config1 = f.read().strip().splitlines()
url = config1[0]
user = config1[1]
pwd = config1[2]

# 不自动关闭浏览器
option = webdriver.ChromeOptions()
option.binary_location = r'.\Chrome\Chrome.exe'  # 指定chrome的路径
option.add_argument('--disable-gpu')  # 禁用gpu加速
option.add_argument('--incognito')  # 隐身模式（无痕模式）
option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
option.add_argument("--headless")  # 无头
option.add_argument("--no-sandbox")  # 解决DevToolsActivePort文件不存在的报错
option.add_argument('--disable-plugins')  # 禁用插件
option.add_experimental_option("detach", True)  # 引入不关闭浏览器的相关配置项
option.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])  # 避免终端下执行代码报警告
option.page_load_strategy = 'eager'  # 加载策略

# 注意此处添加了chrome_options参数
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=option)
driver.get(url)


def openthedoor():
    mobile = driver.find_element_by_id('mobile')
    mobile.clear()
    mobile.send_keys(user)  # 填写帐号

    password = driver.find_element_by_id('password')
    password.send_keys(pwd)  # 填写密码

    js = "let c = document.createElement('canvas');let ctx = c.getContext('2d');" \
         "let img = document.getElementsByTagName('img')[18]; /*找到图片*/ " \
         "c.height=img.naturalHeight;c.width=img.naturalWidth;" \
         "ctx.drawImage(img, 0, 0,img.naturalWidth, img.naturalHeight);" \
         "let base64String = c.toDataURL();return base64String;"
    base64_str = driver.execute_script(js)
    img_bytes = base64.b64decode(str(base64_str).split(",")[1])
    ocr = ddddocr.DdddOcr()  # 实例化
    res = ocr.classification(img_bytes)  # 识别
    print("验证码为" + res)
    verifyCode = driver.find_element_by_id('verifyCode')
    verifyCode.clear()
    verifyCode.send_keys(res)  # 填写验证码

    loginbtn = driver.find_element_by_id('loginbtn')
    loginbtn.click()  # 登录
    errorMsg = driver.find_element_by_id('errorMsg')  # 检测弹窗
    print(errorMsg.text)
    return errorMsg.text


def yijian():
    o = open(cd + '\\1一键登录.bat', 'w')
    o.write('@echo off\n')
    o.write(cd[:2] + '\n')
    o.write('cd ' + cd + '\n')
    o.write('start 一键登录.exe' + '\n')
    o.close()


def kaiji():
    o = open(cd + '\\2开机自启+定时启动（右键管理员运行）.bat', 'w')
    o.write('@echo off\n')
    o.write('schtasks /create /tn "F8登录 开机自启" /tr ' + cd + r'\1一键登录.bat /sc ONLOGON' + '\n')
    o.write('schtasks /create /tn "F8登录8：25" /tr ' + cd + r'\1一键登录.bat /sc daily /st 08:25:00' + '\n')
    o.write('schtasks /create /tn "F8登录17：05" /tr ' + cd + r'\1一键登录.bat /sc daily /st 17:05:00' + '\n')
    o.write('schtasks /create /tn "F8登录23：55" /tr ' + cd + r'\1一键登录.bat /sc daily /st 23:55:00' + '\n')
    o.write('pause')
    o.close()


error = "验证码错误"
while error == "验证码错误":
    driver.refresh()
    error = openthedoor()
else:
    yijian()
    kaiji()
    print("登录成功,3秒后关闭程序")
    driver.quit()
    time.sleep(3)
