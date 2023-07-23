import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='function')  # при каждом новом тесте браузер перезапускается
def driver():
    options = Options()
    options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
