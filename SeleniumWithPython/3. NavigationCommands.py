import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Navigation using webdriver commands
driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")

driver.get("http://newtours.demoaut.com/")  # 1

print(driver.title)

driver.get("http://pawantestingtools.blogspot.in/") # 2
time.sleep(5)
print(driver.title)

driver.back()   # Goes back to 1st page
time.sleep(5)

print(driver.title)

driver.forward()    # Switches to 2nd page
print(driver.title)

driver.quit()