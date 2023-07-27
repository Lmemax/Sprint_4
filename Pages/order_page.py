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
    def  choose_rent_period(self):
        """Выбор периода аренды 1"""
        self.click_on_element(OrderDataLocators.RENT_CLICK)
        self.click_on_element(OrderDataLocators.RENT_PERIOD_INPUT)

    def order_click_on_button_for_order(self, name, surname, address, undeground, phone, date, period, color):
        self.set_text_to_field(UserDataLocators.NAME_INPUT,name)
        self.set_text_to_field(UserDataLocators.SURNAME_INPUT,surname)
        self.set_text_to_field(UserDataLocators.ADDRESS_INPUT,address)
        self.click_on_element(UserDataLocators.UNDEGROUND_INPUT)
        self.click_on_element(undeground)
        self.set_text_to_field(UserDataLocators.PHONE_INPUT,phone)
        self.click_on_element(UserDataLocators.NEXT_BUTTON)
        self.set_text_to_field(OrderDataLocators.DATE_INPUT,date)
        self.choose_rent_period()
        self.click_on_element(period)
        self.click_on_element(color)
        self.click_on_element(OrderDataLocators.MAKE_ORDER_BUTTON)
        self.click_on_element(OrderDataLocators.YES_ORDER_BUTTON)
        self.check_process(OrderDataLocators.MAKED_ORDER_WINDOW)
