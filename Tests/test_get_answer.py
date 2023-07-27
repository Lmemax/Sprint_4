import allure
import pytest
from Pages.main_page import MainPage
from Locators.MainPageLocators import MainPageLocators
import data as h

@allure.feature('Ответы на соответсвующие вопросы')
class TestGetAnswer:
    QUESTIONS_ANSWERS = [(MainPageLocators.PRICE_QUESTION, h.answer0),
                         (MainPageLocators.QUANTITY_QUESTION, h.answer1),
                         (MainPageLocators.RENT_QUESTION, h.answer2),
                         (MainPageLocators.TODAY_ORDER, h.answer3),
                         (MainPageLocators.PROLONGATION_QUESTION, h.answer4),
                         (MainPageLocators.CHARGER_QUESTION, h.answer5),
                         (MainPageLocators.CANCEL_QUESTION, h.answer6),
                         (MainPageLocators.TAKE_QUESTION, h.answer7)]

    @allure.title('Выпадающий список «Вопросы о важном»')
    @allure.description('Проверка,что при клике на вопрос открывается соответствующий ответ')
    @pytest.mark.parametrize('question_locator, expected_answer', QUESTIONS_ANSWERS)
    def test_compare_answer_to_expected_answer(self, driver, main, question_locator, expected_answer):
        page = MainPage(driver)
        page.entry(main[0], main[1], main[2])
        page.get_question(question_locator)
        page.compare_answer_expected_answer(expected_answer)
        assert expected_answer == expected_answer
