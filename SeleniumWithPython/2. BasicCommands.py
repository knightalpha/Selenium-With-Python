import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome
driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")
# driver = webdriver.Chrome(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")


print(driver.title)
print(driver.current_url)
driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button")

time.sleep(5)

# driver.close()    # closes one browser at a time
driver.quit()  # close all tabs
