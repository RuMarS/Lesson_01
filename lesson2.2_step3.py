from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #time.sleep(1)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)

    sum = num1+num2

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))
    #time.sleep(1)

    submitButton = browser.find_element_by_tag_name("button")
    submitButton.click()
    time.sleep(5)

finally:

    browser.quit()




