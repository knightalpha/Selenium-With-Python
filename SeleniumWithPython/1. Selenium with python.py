from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# # driver = webdriver.Chrome(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/chromedriver")

driver = webdriver.Firefox(executable_path="/home/flyboypk/PycharmProjects/SeleniumProject/Drivers/geckodriver")

driver.get("https://www.guru99.com/gecko-marionette-driver-selenium.html")

# print(driver.title)  # title of a page
# print(driver.current_url)   # current url
# # print(driver.page_source)   # returns the source code

# Writes source code into source_code.html file
with open("source_code.html", 'w') as sc:
    sc_reader = sc.writelines(driver.page_source)
    # print(driver.page_source)

# Read from source_code.html
with open("source_code.html", 'r') as sr:
    sr_reader = sr.readlines()
    # for line in enumerate(sr):
    #     print("{}".format(line))

    # c = 1
    # while sr_reader:
    #     print("Line {}: {}".format(c, sr_reader.strip()))
    #     c += 1

    for line in sr_reader:
        print(line)

# driver.close()
