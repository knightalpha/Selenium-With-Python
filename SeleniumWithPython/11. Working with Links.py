"""
1. How many links
2. Capture Links
"""
import time, csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")

driver.get("http://newtours.demoaut.com/")
print(driver.title)
links = driver.find_elements(By.TAG_NAME, "a")  # identify elements in tag_name

print("Number of Links Present:", len(links))

# Read all the links and print one by one
# with open("Links.txt", 'w') as lnk:
#     lnk_writer = csv.writer(lnk)
#     for link in links:
#         csv.writer(lnk_writer,'.txt')
    #     print(link.text)
    #     lnk_writer.write

with open("Links.txt", 'w') as linkk:
    for link in links:
        link_writer = linkk.writelines(link.text)
        print(link.text)
        # linkk.writelines(link.text)

time.sleep(3)
# To click on the link | Using Link text or Partial
# driver.find_element(By.LINK_TEXT, "REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()
# driver.back()


driver.quit()
