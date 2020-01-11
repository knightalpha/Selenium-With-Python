"""
Working with frames
1. switch_to.frame(name)
2. switch_to.frame(id)
"""
import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to_frame("packageListFrame")  # Frame 1

driver.find_element_by_link_text("org.openqa.selenium").click()
driver.switch_to.default_content() # To go back to main page
time.sleep(3)

driver.switch_to_frame("packageFrame")  # Frame 2
driver.find_element_by_link_text("WebDriver").click()   # Click option for frame 2
time.sleep(3)

driver.switch_to.default_content() # To go back to main page

driver.switch_to_frame("classFrame")  # Frame 2
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click() # TO go to Depricated
time.sleep(3)

driver.quit()