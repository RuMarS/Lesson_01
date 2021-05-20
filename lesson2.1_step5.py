from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)


    x = browser.find_element_by_id("input_value")
    x = x.text
    x = math.log(math.fabs(12*math.sin(float(x))))
    textField = browser.find_element_by_id("answer")
    textField.send_keys(str(x))
    time.sleep(2)

    chB = browser.find_element_by_id("robotCheckbox")
    chB.click()
    time.sleep(2)

    rB = browser.find_element_by_id("robotsRule")
    rB.click()
    time.sleep(2)

    submitButton = browser.find_element_by_tag_name("button")
    submitButton.click()
    time.sleep(2)

finally:

    browser.quit()




