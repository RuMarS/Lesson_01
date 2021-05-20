from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    btn = browser.find_element_by_tag_name("button")
    btn.click()
    time.sleep(1)

    confirmWindow=browser.switch_to.alert
    confirmWindow.accept()
    time.sleep(1)

    x = int(browser.find_element_by_id("input_value").text)
    ans = browser.find_element_by_id("answer")
    ans.send_keys(str(math.log(abs(12*math.sin(x)))))
    time.sleep(1)

    submitBtn = browser.find_element_by_tag_name("button")
    submitBtn.click()


finally:
    time.sleep(2)
    res = (browser.switch_to.alert.text).split(": ")
    print(res[-1])
    browser.quit()