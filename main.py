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
    def __init__(self):
        self.driver_chrome = None

    def open_browser(self):
        # открытие браузера с параметрами
        self.driver_chrome = webdriver.Chrome(
            options=options,
            service=service
        )
        # переход по url в браузере/развернуть на весь экран
        self.driver_chrome.get(base_url)
        self.driver_chrome.maximize_window()
        print("Браузер открыт.")


start_test = Test()
start_test.open_browser()
