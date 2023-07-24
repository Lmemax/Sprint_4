from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        self.driver.find_element(*locator)

    def wait_for_loading_page(self, locator):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(*locator))

    def wait_for_load_new_page(self, url):
        WebDriverWait(self.driver, 5).until(ec.url_to_be(url))

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def open_new_window(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def set_text_to_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def check_order_process(self, locator):
        text = self.driver.find_element(*locator).text
        return text
