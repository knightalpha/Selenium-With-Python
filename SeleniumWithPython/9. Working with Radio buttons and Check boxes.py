from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Working with Radio Buttons
status = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()  # False
print(status)

driver.find_element_by_id("RESULT_RadioButton-8_0").click()  # Select radio btn

status = driver.find_element_by_id("RESULT_RadioButton-8_0").is_selected()  # True/False
print(status)

# # Working with check boxes
driver.find_element_by_id("RESULT_CheckBox-8_0").click()
driver.find_element_by_id("RESULT_CheckBox-8_6").click()

status1 = driver.find_element_by_id("RESULT_CheckBox-8_6").is_selected()
print(status1)


driver.quit()
