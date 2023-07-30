import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Locators.MainPageLocators import MainPageLocators
from Pages.base_page import BasePage
import data as h



class MainPage(BasePage):

    @allure.step('Ожидание загрузки главной страницы')
    def entry(self):
        self.open_test_web_url(h.main_page)
        self.wait_for_loading_page(MainPageLocators.TAKE_QUESTION)

    @allure.step('Принять куки')
    def add_cookies(self):
        self.click_on_element(MainPageLocators.BUTTON_COOKIES)

    @allure.step('Нажать на кнопку Заказать в header главной страницы')
    def click_order_button_header(self):
        self.click_on_element(MainPageLocators.BUTTON_HEADER_ORDER)

    @allure.step('Нажать на кнопку Заказать на главной страницы')
    def click_order_button_on_page(self):
        self.click_on_element(MainPageLocators.BUTTON_FINISH_ORDER)

    @allure.step('Нажать на логотип Яндекса в header главной страницы')
    def click_logo_yandex(self):
        """Проверка перехода на сайт Яндекс"""
        self.click_on_element(MainPageLocators.LOGO_YANDEX)
        self.open_new_window()
        self.wait_for_load_new_page(url=h.yandex)

    @allure.step('Найти интересующий вопрос')
    def get_question(self, question_locator):
        """Поиск вопроса"""
        self.scroll_to(question_locator)
        self.click_on_element(question_locator)

    @allure.step('Найти расскрытый вопрос с ответом на него')
    def find_not_hidden_answer(self):
        """Получение текста ответа на вопрос"""
        self.wait_for_loading_page(MainPageLocators.TAKE_QUESTION)
        self.get_text(MainPageLocators.OPEN_ANSWER)
        return self.get_text(MainPageLocators.OPEN_ANSWER)

    @allure.step('Получить расскрытый ответ')
    def compare_answer_expected_answer(self, expected_answer):
        self.find_not_hidden_answer()
