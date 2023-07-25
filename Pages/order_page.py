import allure
from Locators.OrderLocators import UserDataLocators
from Locators.OrderLocators import OrderDataLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Pages.base_page import BasePage
import data as h


class OrderData(BasePage):

    def transition(self, url, push):
        self.open_test_web_url(url)
        self.click_on_element(push)


    def order_click_on_button_header(self, name, surname, address, phone, date):
        """шаг по оформлению заказа при нажатии кнопки заказать в header"""
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choose_undeground_station_1()
        self.input_phone(phone)
        self.click_on_next_button()
        self.input_date(date)
        self.choose_rent_period_1()
        self.choose_color_1()
        self.click_on_make_order_button()
        self.confirm_order()
        self.check_order_process()
        self.check_status()

    def order_on_page_button(self, name, surname, address, phone, date):
        """шаг по оформлению заказа при нажатии кнопки заказать на главной странице"""
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choose_undeground_station_2()
        self.input_phone(phone)
        self.click_on_next_button()
        self.input_date(date)
        self.choose_rent_period_2()
        self.choose_color_2()
        self.click_on_make_order_button()
        self.confirm_order()
        self.check_order_process()
        self.check_status()
