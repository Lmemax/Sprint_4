import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Locators.MainPageLocators import MainPageLocators
from Pages.base_page import BasePage
import data as h



class MainPage(BasePage):
    QUESTIONS_ANSWERS = [(MainPageLocators.PRICE_QUESTION, h.answer0),
                             (MainPageLocators.QUANTITY_QUESTION, h.answer1),
                             (MainPageLocators.RENT_QUESTION, h.answer2),
                             (MainPageLocators.TODAY_ORDER, h.answer3),
                             (MainPageLocators.PROLONGATION_QUESTION, h.answer4),
                             (MainPageLocators.CHARGER_QUESTION, h.answer5),
                             (MainPageLocators.CANCEL_QUESTION, h.answer6),
                             (MainPageLocators.TAKE_QUESTION, h.answer7)]


    def entry(self, url, locator):
        """шаг готовности к работе с сайтом"""
        self.open_url(url)
        self.wait_for_loading_page(*Ь)
        self.click_on_element()


    @allure.step('Нажать на логотип Яндекса в header главной страницы')
    def click_logo_yandex(self):
        """Проверка перехода на сайт Яндекс"""
        self.click_on_element()
        self.open_new_window()
        self.wait_for_load_new_page()

    @allure.step('Найти интересующий вопрос')
    def get_question(self, question_locator):
        """Поиск вопроса"""
        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()

    @allure.step('Найти расскрытый вопрос с ответом на него')
    def find_not_hidden_answer(self):
        """Получение текста ответа на вопрос"""
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.TAKE_QUESTION))
        self.answer = self.driver.find_element(*MainPageLocators.OPEN_ANSWER).text
        return self.answer

    @allure.step('Получить расскрытый ответ')
    def compare_answer_expected_answer(self, expected_answer):
        self.find_not_hidden_answer()
