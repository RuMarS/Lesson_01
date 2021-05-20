from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))

    btn = browser.find_element_by_id("book")
    btn.click()

    """newTab=browser.switch_to.window(browser.window_handles[-1])
    #time.sleep(1)"""

    x = int(browser.find_element_by_id("input_value").text)
    ans = browser.find_element_by_id("answer")
    ans.send_keys(str(math.log(abs(12*math.sin(x)))))
    #time.sleep(1)

    submitBtn = browser.find_element_by_id("solve")
    submitBtn.click()


finally:
    #time.sleep(2)
    res = (browser.switch_to.alert.text).split(": ")
    print(res[-1])
    browser.quit()