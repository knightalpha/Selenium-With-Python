from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")

driver.get("http://newtours.demoaut.com/")  # 1

# wait some time here
driver.implicitly_wait(10)  # Seconds

assert "Welcome: Mercury Tours" in driver.title

ele = driver.find_element_by_name("userName").send_keys("mercury")

ele1 = driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()

driver.quit()
