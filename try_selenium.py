from selenium import webdriver
import time
import requests
from 云打码示例 import YDMHTTP

#  如果路径带中文或者带'\U'路径前加r，如webdriver的路径为'\User\XXX\XXXdriver'，则这里路径为r"\User\XXX\XXXdriver"
#  IE浏览器,以下是等价的,即webdriver不是一定要放到相应浏览器的安装目录，可以将我们要用的webdriver放在一起便于管理
# browser = webdriver.Ie(r"E:\software\编程相关\browserDrivers\IEDriverServer.exe")
# browser = webdriver.Ie(r"C:\Users\TvVc\Desktop\IEDriverServer.exe")
# browser = webdriver.Ie("C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe")
# driver = webdriver.Ie(r"D:\IEDriver\IEDriverServer.exe")
# browser = webdriver.Ie()  #需要将IEDriverServer.exe放置在python的安装文件夹，比如"C:\Python36\IEDriverServer.exe"


#  Chrome浏览器，没有找到官方win64位的webdriver
driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe")
# browser = webdriver.Chrome(r"E:\software\编程相关\browserDrivers\chromedriver.exe")
# browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# browser = webdriver.Chrome()  #需要将chromedriver.exe放在python的安装文件夹如"C:\Python36\chromedriver.exe"


#  Edge浏览器
# driver = webdriver.Edge(r"D:\EdgeDriver\MicrosoftWebDriver.exe")
# browser = webdriver.Edge("C:\Windows\SystemApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\MicrosoftWebDriver.exe")
# browser = webdriver.Edge(r"E:\software\编程相关\browserDrivers\MicrosoftWebDriver.exe")
# browser = webdriver.Edge() #需要将MicrosoftWebDriver.exe放在python的安装文件夹如"C:\Python36\MicrosoftWebDriver.exe"
# browser.get("https://cn.bing.com/")


# PhantomJS
# driver = webdriver.PhantomJS(r"D:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe")
# browser = webdriver.PhantomJS("C:\Windows\SystemApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\MicrosoftWebDriver.exe")
# browser = webdriver.PhantomJS(r"E:\software\编程相关\browserDrivers\MicrosoftWebDriver.exe")
# browser = webdriver.PhantomJS() #需要将MicrosoftWebDriver.exe放在python的安装文件夹如"C:\Python36\MicrosoftWebDriver.exe"
# browser.get("https://cn.bing.com/")
# 实例化一个浏览器

# 发送请求
# driver = webdriver.PhantomJS()
# 设置窗口大小
driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.get("https://www.baidu.com")
# 进行页面截屏
driver.save_screenshot("百度.png")
# 确定元素位置
# driver.find_element_by_id("kw").send_keys("darren573")
# driver.find_element_by_id("su").click()  # 点击一下
# driver获取cookie
# cookies = driver.get_cookies()
# print(cookies)
# print("*" * 100)
# cookies = {i["name"]: i["value"] for i in cookies}
# print(cookies)


# 识别验证码
captcha_image_url = driver.find_element_by_id("id_name").get_attribute("src")  # 获取验证码图片的url
captcha_content = requests.get(captcha_image_url).content
captcha_code = YDMHTTP.indetify(captcha_content)
print("验证码的识别结果为：", captcha_code)

# 输入验证码
driver.find_element_by_id("id_name").send_keys(captcha_code)


print(driver.page_source)  # 浏览器中element的内容
time.sleep(5)
# 退出浏览器
driver.quit()
