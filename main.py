from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Test:
    def __init__(self, base_url):
        self.driver_chrome = None
        self.base_url = base_url
        self.options = self.configuration()
        self.service = ChromeService(ChromeDriverManager().install())

    def configuration(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return options

    def open_browser(self):
        # открытие браузера с параметрами
        self.driver_chrome = webdriver.Chrome(
            options=self.options,
            service=self.service
        )
        # переход по url в браузере/развернуть на весь экран
        self.driver_chrome.get(base_url)
        self.driver_chrome.maximize_window()
        print("Браузер открыт.")


if __name__ == "__main__":
    base_url = 'https://www.saucedemo.com/'
    start_test = Test(base_url)
    start_test.open_browser()


