import allure
from Pages.main_page import MainPage
from Pages.order_page import OrderData
from Locators.MainPageLocators import MainPageLocators
import data as h


class TestTransitions:

    @allure.title('Проверка клика на логотип Яндекса c главной страницы')
    @allure.description('На странице ищем логотип Яндекс и проверяем, что кликнув на него откроется новая вкладка Дзен')
    def test_click_on_logo_yandex(self, driver, worker):
        """Проверка перехода на сайт Яндекс c главной страницы сайта Самокат"""
        page = MainPage(driver)
        page.entry(worker[0], worker[1], worker[2])
        page.click_logo_yandex()
        assert driver.current_url == h.yandex

    @allure.title('Проверка клика на логотип Самокат со страницы оформления заказа')
    @allure.description('При клике на логотип Самокат происходит переход на главную страницу')
    def test_click_on_logo_scooter(self, driver):
        """Проверка перехода по клику на логотип сайта Самокат"""
        page = OrderData(driver)
        page.open_user_data_url()
        page.click_logo_scooter()
        page = MainPage(driver)
        page.wait_for_load_home_page()
        assert driver.current_url == h.main_page and driver.find_element(*MainPageLocators.TAKE_QUESTION).is_displayed()
