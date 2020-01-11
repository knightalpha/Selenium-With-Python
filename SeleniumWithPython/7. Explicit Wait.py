import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")

driver.implicitly_wait(5)   # Implicit wait is applicable for all element
driver.maximize_window()    # Maximize the window

driver.get("https://www.expedia.com/")

# driver.find_element_by_id(By.ID, "tab-flight-tab-hp").click() # Flight Button
# OR
driver.find_element(By.ID, "tab-flight-tab-hp").click() # Flight Button

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("DEL")  # Origin

time.sleep(2)   # from python

driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("BOM") # Destination

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("01/26/2020")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("01/29/2020")

driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()
# driver.find_elements(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']").click()

# Explicit wait statement
wait = WebDriverWait(driver, 10)    # Max time for the webdriverwait to wait

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
element.click()
time.sleep(3)

driver.quit()
