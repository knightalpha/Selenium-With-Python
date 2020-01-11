"""
Working with alerts
1. accept
2. dismiss
"""
import time, csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")

driver.get("https://testautomationpractice.blogspot.com")

driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()

time.sleep(5)

# driver.switch_to_alert().accept()   # Close alert window using ok button

driver.switch_to_alert().dismiss() # CLose alert by using cancel button

driver.close()