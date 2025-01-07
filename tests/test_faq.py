import allure
import pytest
from locators import HomePageLocators
from constants import ExpectedAnswer
from pages.home_page import HomePage

class TestFaq:
    @allure.title('Проверка видимости ответа, при нажатии на вопрос')
    @allure.description('По очереди проверяем раскрытие ответа, при нажатии на вопрос, сравниваем полученный текст ответа с ожидаемым')
    @pytest.mark.parametrize("number_question, number_answer, expected_answer",
        [
            (0, 0, ExpectedAnswer.answer_1),
            (1, 1, ExpectedAnswer.answer_2),
            (2, 2, ExpectedAnswer.answer_3),
            (3, 3, ExpectedAnswer.answer_4),
            (4, 4, ExpectedAnswer.answer_5),
            (5, 5, ExpectedAnswer.answer_6),
            (6, 6, ExpectedAnswer.answer_7),
            (7, 7, ExpectedAnswer.answer_8),
        ]
    )
    def test_click_faq_questions_show_answers(self, driver, number_question, number_answer, expected_answer):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie()
        home_page.click_faq_question(number_question)
        answer = home_page.find_element(HomePageLocators.FAQ_ANSWER(number_answer))
        assert answer.is_displayed() and answer.text == expected_answer , f"Ответ не видно"
