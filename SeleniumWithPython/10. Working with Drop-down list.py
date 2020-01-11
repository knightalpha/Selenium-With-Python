from selenium import webdriver
from selenium.webdriver.support.ui import Select

"""
1. Select one option
2. Find out how many options exist in drop down
3. Count how many options are present
"""
driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")
# driver = webdriver.Chrome(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")  # Select class
drp = Select(element)

# # Select by visible text
# drp.select_by_visible_text('Morning')  # Select Morning

# Select by index
# drp.select_by_index(2)  # Afternoon it will select
drp.select_by_index(3)

# # Select by Value
# drp.select_by_value("Radio-2")

# Count no of options
print(len(drp.options))


# Capture all the options and print them as output
AllOptions = drp.options
for option in AllOptions:
    print(option.text)

driver.quit()