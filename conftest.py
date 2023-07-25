import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from Locators.MainPageLocators import MainPageLocators
from Locators.OrderLocators import UserDataLocators
import data as h


@pytest.fixture(scope='function')  # при каждом новом тесте браузер перезапускается
def driver():
    options = Options()
    options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture  # загрузка главной страницы с принятием куки
def main():
    main = [h.main_page, MainPageLocators.TAKE_QUESTION,MainPageLocators.BUTTON_COOKIES]
    return main

@pytest.fixture
def order():  # данные для перехода со страницы заказа по клику на логотип сайта
    order = [h.order_data, UserDataLocators.LOGO_SCOOTER,MainPageLocators.TAKE_QUESTION]
    return order
