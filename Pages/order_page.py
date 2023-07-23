import allure
from Locators.OrderLocators import UserDataLocators
from Locators.OrderLocators import OrderDataLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Pages.base_page import BasePage
import helpers as h


class OrderData(BasePage):

    @allure.step('Переход на страницу заказа')
    def open_user_data_url(self):
        self.driver.get(h.order_data)
    @allure.step('Ожидание загрузки страницы заказа')
    def wait_for_load_user_data_page(self):
        """ожидание загрузки страницы для ввода данных заказчика"""
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(UserDataLocators.NEXT_BUTTON))

    def logo_scooter(self):
        return self.driver.find_element(*UserDataLocators.LOGO_SCOOTER)

    @allure.step('Нажать на логотип Самокат в header страницы заказа')
    def click_logo_scooter(self):
        """Проверка перехода на клику на логотип сайта"""
        self.logo_scooter().click()

    # Ввод данных пользователя
    @allure.step('Ввод имени заказчика')
    def input_name(self, name):
        """Ввод имени"""
        self.driver.find_element(*UserDataLocators.NAME_INPUT).send_keys(name)

    @allure.step('Ввод фамилии заказчика')
    def input_surname(self, surname):
        """Ввод фамилии"""
        self.driver.find_element(*UserDataLocators.SURNAME_INPUT).send_keys(surname)

    @allure.step('Ввод адреса доставки')
    def input_address(self, address):
        """Ввод адреса"""
        self.driver.find_element(*UserDataLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step('Выбор станции метро 1')
    def choose_undeground_station_1(self):
        """Выбор станции метро 1"""
        self.driver.find_element(*UserDataLocators.UNDEGROUND_INPUT).click()
        self.driver.find_element(*UserDataLocators.UNDEGROUND_STATION_1).click()

    @allure.step('Выбор станции метро 2')
    def choose_undeground_station_2(self):
        """Выбор станции метро 2"""
        self.driver.find_element(*UserDataLocators.UNDEGROUND_INPUT).click()
        self.driver.find_element(*UserDataLocators.UNDEGROUND_STATION_2).click()

    @allure.step('Ввод номера телефона заказчика')
    def input_phone(self, phone):
        """Ввод номера телефона"""
        self.driver.find_element(*UserDataLocators.PHONE_INPUT).send_keys(phone)

    @allure.step('Нажатие кнопки далее')
    def click_on_next_button(self):
        """Нажатие на кнопку далее"""
        self.driver.find_element(*UserDataLocators.NEXT_BUTTON).click()

    # Ввод данных заказа
    @allure.step('Выбор даты достаки')
    def input_date(self, date):
        """Выбор даты доставки"""
        self.driver.find_element(*OrderDataLocators.DATE_FIELD).click()
        self.driver.find_element(*OrderDataLocators.DATE_INPUT).send_keys(date)

    @allure.step('Выбор срока аренды 1')
    def  choose_rent_period_1(self):
        """Выбор периода аренды 1"""
        self.driver.find_element(*OrderDataLocators.RENT_CLICK).click()
        self.driver.find_element(*OrderDataLocators.RENT_PERIOD_INPUT).click()
        self.driver.find_element(*OrderDataLocators.RENT_PERIOD_1_DAY).click()

    @allure.step('Выбор срока аренды 2')
    def choose_rent_period_2(self):
        """Выбор периода аренды 2"""
        self.driver.find_element(*OrderDataLocators.RENT_CLICK).click()
        self.driver.find_element(*OrderDataLocators.RENT_PERIOD_INPUT).click()
        self.driver.find_element(*OrderDataLocators.RENT_PERIOD_5_DAYS).click()

    @allure.step('Выбор цвета 1')
    def choose_color_1(self):
        """Выбор цвета 1"""
        self.driver.find_element(*OrderDataLocators.COLOR_CHOICE_BLACK).click()

    @allure.step('Выбор цвета 2')
    def choose_color_2(self):
        """Выбор цвета 2"""
        self.driver.find_element(*OrderDataLocators.COLOR_CHOICE_GREY).click()

    @allure.step('Нажать кпнопку заказать')
    def click_on_make_order_button(self):
        """нажатие на кнопку заказать"""
        self.driver.find_element(*OrderDataLocators.MAKE_ORDER_BUTTON).click()

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        """нажатие на кнопку Да для подтверждения заказа"""
        self.driver.find_element(*OrderDataLocators.YES_ORDER_BUTTON).click()

    @allure.step('Получение информации о оформлении заказа')
    def check_order_process(self):
        """возврат информации о том, что заказ создан"""
        text = self.driver.find_element(*OrderDataLocators.MAKED_ORDER_WINDOW).text
        return text

    @allure.step('Проверка, что кнопка посмотреть статус присутствует в окне информации о оформлении')
    def check_status(self):
        """кнопка проверить статус заказа отображается"""
        self.driver.find_element(*OrderDataLocators.VIEW_STATUS_BUTTON).is_displayed()

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
