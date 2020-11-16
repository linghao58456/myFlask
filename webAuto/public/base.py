from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def open_browser(self, browser):
        if browser == "google":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            # noinspection PyAttributeOutsideInit
            self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        return self.driver

    def get_url(self, url):
        self.driver.get(url)

    def find_element(self, key, value):
        locator = (key, value)
        try:
            element = WebDriverWait(self.driver, 5, 0.5).until(ec.presence_of_element_located(locator))
            return element
        except Exception as e:
            print(str(e))

    def send_key_value(self, key, value, name):
        element = self.find_element(key, value)
        element.send_keys(name)

    def click_btn(self, key, value):
        element = self.find_element(key, value)
        element.click()

    def get_text_value(self, key, value):
        element = self.find_element(key, value)
        return element.text


if __name__ == '__main__':
    base = Base()
    base.open_browser("google")
    base.get_url("http://baidu.com")
    a = base.get_text_value("id", "su")
    print(a)
