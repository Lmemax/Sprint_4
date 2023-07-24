import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Locators.MainPageLocators import MainPageLocators
from Pages.base_page import BasePage
import data as h



class MainPage(BasePage):

    def entry(self, url, wait, push):
        """шаг готовности к работе с сайтом"""
        self.open_test_web_url(url)
        self.wait_for_loading_page(wait)
        self.click_on_element(push)


    @allure.step('Нажать на логотип Яндекса в header главной страницы')
    def click_logo_yandex(self):
        """Проверка перехода на сайт Яндекс"""
        self.click_on_element(MainPageLocators.LOGO_YANDEX)
        self.open_new_window()
        self.wait_for_load_new_page(url=h.yandex)

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
