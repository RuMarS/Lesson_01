from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Вася")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Пупкин")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("pupkin.vasya@gmail.com")

    import os

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'someText.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла