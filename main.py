from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://www.saucedemo.com/'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())


class Test():
    def open_browser(self):
        # открытие браузера с параметрами
        driver_chrome = webdriver.Chrome(
            options=options,
            service=service
        )
        # переход по url в браузере/развернуть на весь экран
        driver_chrome.get(base_url)
        driver_chrome.maximize_window()
        print("Браузер открыт.")


start_test = Test()
start_test.open_browser()
