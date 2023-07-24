import allure
import pytest
from Pages.order_page import OrderData
from Pages.main_page import MainPage
import data as h


class TestAddOrder:

    @allure.title('Оформление заказа при нажатии кнопки в header главной страницы')
    @allure.description('Проверка открытия, заполнения данных для заказа самоката и информации о успешном заказе')
    @pytest.mark.parametrize('name,surname,address,phone,date', h.user_data)
    def test_add_order_click_on_button_header(self, driver, name, surname, address, phone, date):
        page = MainPage(driver)
        page.entry()
        page.click_order_button_header()
        page = OrderData(driver)
        page.order_click_on_button_header(name, surname, address, phone, date)
        assert 'Заказ оформлен' in page.check_order_process()

    @allure.title('Оформление заказа при нажатии кнопки на главной странице')
    @allure.description('Проверка открытия, заполнения данных для заказа самоката и информации о успешном заказе')
    @pytest.mark.parametrize('name,surname,address,phone,date', h.user_data)
    def test_add_order_click_on_page_button(self, driver, name, surname, address, phone, date):
        page = MainPage(driver)
        page.entry()
        page.click_order_button_header()
        page = OrderData(driver)
        page.order_on_page_button(name, surname, address, phone, date)
        assert 'Заказ оформлен' in page.check_order_process()
