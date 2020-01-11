import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# driver.find_element(By.CLASS_NAME, 'text_field')

# How to find how many input boxes present in web page
inputBoxes = driver.find_elements(By.CLASS_NAME, 'text_field')

print(len(inputBoxes))  # 8

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("displayed ", status)

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print("enabled ", status)

# How to provide values in the text box
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Peekay")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("Alpha")
driver.find_element_by_id('RESULT_TextField-3').send_keys("9999999999")


driver.quit()