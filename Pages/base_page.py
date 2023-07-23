class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_main_url(self, url):
        self.driver.get(url)
