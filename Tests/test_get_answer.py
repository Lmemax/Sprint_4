import allure
import pytest
from Pages.main_page import MainPage


class TestGetAnswer:

    @allure.title('Выпадающий список «Вопросы о важном»')
    @allure.description('Проверка,что при клике на вопрос открывается соответствующий ответ')
    @pytest.mark.parametrize('question_locator, expected_answer', MainPage.QUESTIONS_ANSWERS)
    def test_compare_answer_to_expected_answer(self, driver, question_locator, expected_answer):
        page = MainPage(driver)
        page.entry()
        page.get_question(question_locator)
        page.compare_answer_expected_answer(expected_answer)
        assert expected_answer == page.find_not_hidden_answer()
