"""Демонстрация привязки селекторов к конкретным элементам,
чтобы в случае внезапного изменения было понятно на чем робот падает."""
import time
from selenium import webdriver as driver


# Генерировать трассировку при потере элемента? True/False
TRACE = True
# Заполнять только обязательные поля?
REQUIRED_FIELDS = True


class ChromeDriver:
    """Объект Chrome driver."""
    def __init__(self):
        print("Инициализирую Chrome object...")
        # Объект браузера
        self.browser = driver.Chrome(chrome_options=self.chrome_options())
        # Статус выполнения задачи
        self.status = False
        print("Инициализация Chrome object завершена.")

    def chrome_options(self):
        """Настройка Chrome browser"""
        print("Устанавливаю настройки для Chrome browser...")
        options = driver.ChromeOptions()
        # При запуске разворачивать на весь экран
        options.add_argument("--start-maximized")
        # Отключить уведомления об автоматическом режиме
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        print("Настройки для Chrome browser установлены.")
        return options

    def wait_element_by_xpath(self, element, time_wait: int=30, reraise=False) -> bool:
        """Проверяет доступен ли элемент по xpath.\n
        * time_wait - сколько ждем (30сек.)\n
        * reraise - бросать ли исключение (False)"""
        while not self.browser.find_elements_by_xpath(element) and time_wait > 0:
            time.sleep(1)
            time_wait -= 1
        # Если время ожидания не истекло до обнаружения элемента - это успех. Иначе - либо False, либо Exception.
        if time_wait:
            return True
        else:
            if not reraise:
                return False
            else:
                # Генерирую ошибку
                self.browser.find_element_by_xpath(element)

    def registration(self, link):
        """Задача к уроку 1.6 - форма регистрации.\n
        * link - ссылка на форму регистрации"""
        print("----------------------------------------------------")
        print("Выполняю задачу к уроку 1.6 - форма регистрации...")
        print("Получена на вход ссылка на форму: ", link)
        # Обнуляю статус
        self.status = False
        # Перехожу на страницу
        self.browser.get(link)
        # Убеждаюсь что страница готова, загрузился нужный элемент
        check_selector = '//h1[text()="Registration"]'
        if self.wait_element_by_xpath(check_selector, time_wait=5, reraise=TRACE):
            print("Страница загружена. Ввожу данные и получаю ответ...")
            try:
                # Заполняю поля
                self.browser.find_element_by_xpath('//label[text()="First name*"]/following::input').send_keys("Ivan")
                self.browser.find_element_by_xpath('//label[text()="Last name*"]/following::input').send_keys("Vikharev")
                self.browser.find_element_by_xpath('//label[text()="Email*"]/following::input').send_keys("Ivan@mail.ru")
                # Необязательные поля
                if not REQUIRED_FIELDS:
                    self.browser.find_element_by_xpath('//label[text()="Phone:"]/'
                                                       'following::input').send_keys("890847495777")
                    self.browser.find_element_by_xpath('//label[text()="Address:"]/'
                                                       'following::input').send_keys("Nizhny Novgorod")
                # Нажимаю кнопку 'Submit'
                self.browser.find_element_by_xpath('//button[text()="Submit"]').click()
                # Печатаю результат
                time_temp, result = 30, ""
                while time_temp:
                    try:
                        time.sleep(1)
                        result = self.browser.find_element_by_xpath('//h1').text
                        self.status = True
                        break
                    except Exception:
                        time_temp -=1
                print(f"Получен результат: [{result}]")
            except Exception as ex:
                if TRACE:
                    print(f"Не удалось получить результат! Трассировка: [{ex}].")
                    self.status = False
                else:
                    print(f"Не удалось получить результат! Проверьте селектора.")
                    self.status = False
        # Если элемент не доступен
        else:
            print(f"Не удалось загрузить страницу! Не валидный селектор: [{check_selector}].")

        print(f"Задача к уроку 1.6 - форма регистрации завершена {'УСПЕШНО' if self.status else 'НЕУДАЧНО'}.")
        print("----------------------------------------------------")

    def __del__(self):
        # Закрываю браузер и драйвер
        try:
            self.browser.close()
            self.browser.quit()
        except Exception:
            pass


if __name__ == "__main__":
    print("===== СТАРТ =====")

    try:
        browser = ChromeDriver()
        # Пробую считать registration1
        browser.registration("http://suninjuly.github.io/registration1.html")
        # Пробую считать registration2
        browser.registration("http://suninjuly.github.io/registration2.html")
    except Exception as ex:
        print(f"Системная ошибка: [{ex}].")

    print("===== КОНЕЦ =====")
    