import allure
import pytest
from Pages.order_page import OrderData
from Pages.main_page import MainPage
from Locators.MainPageLocators import MainPageLocators
from Locators.OrderLocators import OrderDataLocators
import data as h


@allure.feature('Оформление заказа')
class TestAddOrder:

    @allure.title('Оформление заказа при нажатии кнопки в header главной страницы')
    @allure.description('Проверка открытия, заполнения данных для заказа самоката и информации о успешном заказе')
    @pytest.mark.parametrize('name,surname,address,undeground,phone,date,period,color', h.user_data)
    def test_add_order_click_on_button_header(self, driver, main, name, surname,
                                              address, undeground, phone, date, period, color):
        page = MainPage(driver)
        page.entry(main[0], main[1], main[2])
        page.click_on_element(MainPageLocators.BUTTON_HEADER_ORDER)
        page = OrderData(driver)
        page.order_click_on_button_for_order(name, surname,
                                             address, undeground, phone, date, period, color)
        assert 'Заказ оформлен' in page.get_text(OrderDataLocators.MAKED_ORDER_WINDOW), 'Нет подтверждения, что заказ' \
                                                                                        'оформлен.'

    @allure.title('Оформление заказа при нажатии кнопки на главной странице')
    @allure.description('Проверка открытия, заполнения данных для заказа самоката и информации о успешном заказе')
    @pytest.mark.parametrize('name,surname,address,undeground,phone,date,period,color', h.user_data)
    def test_add_order_click_on_page_button(self, driver, main, name, surname,
                                            address, undeground, phone, date, period, color):
        page = MainPage(driver)
        page.entry(main[0], main[1], main[2])
        page.click_on_element(MainPageLocators.BUTTON_FINISH_ORDER)
        page = OrderData(driver)
        page.order_click_on_button_for_order(name, surname,
                                             address, undeground, phone, date, period, color)
        assert 'Заказ оформлен' in page.get_text(OrderDataLocators.MAKED_ORDER_WINDOW), 'Нет подтверждения, что заказ' \
                                                                                        'оформлен.'
