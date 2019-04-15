from selenium import webdriver
import time

driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe")
driver.get("http://www.renren.com/")
time.sleep(1)
driver.find_element_by_id("email").send_keys("13938386255")
time.sleep(1)
driver.find_element_by_id("password").send_keys("darren573")
time.sleep(2)
driver.find_element_by_class_name("login").click()
cookies = {i["name"]: i["value"] for i in driver.get_cookies()}
print(cookies)
driver.save_screenshot("人人.png")
time.sleep(15)
driver.quit()
