from selenium import webdriver
import time

driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe")
driver.get("https://accounts.douban.com/passport/login_popup?login_source=anony")
time.sleep(1)
driver.find_element_by_class_name("account-tab-account").click()
time.sleep(1)
driver.find_element_by_id("username").send_keys("13938386255")
time.sleep(1)
driver.find_element_by_id("password").send_keys("Lse950825.com")
time.sleep(2)
driver.find_element_by_xpath("//div[@class='account-form']/div[5]").click()
cookies = {i["name"]: i["value"] for i in driver.get_cookies()}
print(cookies)
time.sleep(2)
driver.save_screenshot("豆瓣.png")
time.sleep(10)
driver.quit()
