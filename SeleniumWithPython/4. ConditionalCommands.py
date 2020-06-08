from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")

driver.get("http://newtours.demoaut.com/")  # 1
# driver.get("https://github.com/login")

ele = driver.find_element_by_name("userName")
print(ele.is_displayed())  # returns true/false based on element status
print(ele.is_enabled())  # returns true or false

ele1 = driver.find_element_by_name("password")
print(ele1.is_displayed())
print(ele1.is_enabled())

ele.send_keys("mercury")
ele1.send_keys("mercury")

driver.find_element_by_name("login").click()

# ele = driver.find_element_by_name("login")

# ele1 = driver.find_element_by_name("password")

roundtrip_radio_button = driver.find_element_by_css_selector("input[value = roundtrip]")
print("Status of round trip radio button", roundtrip_radio_button.is_selected())

onetrip_radio = driver.find_element_by_css_selector("input[value = oneway]")
print("Status of one trip radio button", onetrip_radio.is_selected())   # print status of radio button


# ele.send_keys("pk.airsqn@gmail.com")
# ele1.send_keys("password")

# driver.find_element_by_name("commit").click()
driver.quit()
