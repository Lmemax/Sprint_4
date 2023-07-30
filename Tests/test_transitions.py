import allure
from Pages.main_page import MainPage
from Pages.order_page import OrderData
from Locators.MainPageLocators import MainPageLocators
from Locators.OrderLocators import UserDataLocators
import data as h


@allure.feature('Проверка перехода по клику на логотип')
class TestTransitions:

    @allure.title('Проверка клика на логотип Яндекса c главной страницы')
    @allure.description('На странице ищем логотип Яндекс и проверяем, что кликнув на него откроется новая вкладка Дзен')
    def test_click_on_logo_yandex(self, driver):
        """Проверка перехода на сайт Яндекс c главной страницы сайта Самокат"""
        page = MainPage(driver)
        page.entry()
        page.add_cookies()
        page.click_logo_yandex()
        assert driver.current_url == h.yandex

    @allure.title('Проверка клика на логотип Самокат со страницы оформления заказа')
    @allure.description('При клике на логотип Самокат происходит переход на главную страницу')
    def test_click_on_logo_scooter(self, driver):
        """Проверка перехода по клику на логотип сайта Самокат"""
        page = OrderData(driver)
        page.open_test_web_url(h.order_data)
        page.click_on_element(UserDataLocators.LOGO_SCOOTER)
        page.wait_for_loading_page(MainPageLocators.TAKE_QUESTION)
        assert driver.current_url == h.main_page and driver.find_element(*MainPageLocators.TAKE_QUESTION).is_displayed()
