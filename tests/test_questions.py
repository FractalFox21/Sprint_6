import pages.home_page
import locators
from pages.home_page import HomePage
from conftest import driver


class TestQuestions():

    @pytest.mark.parametrize(
        'question, answer',[
        ['Q_HOW_MUCH', 'ANS_HOW_MUCH'],
        ['Q_SOME_SCOOTERS' , 'ANS_SOME_SCOOTERS'],
        ['Q_RENTAL_TIME', 'ANS__RENTAL_TIME'],
        ['Q_SCOOTER_TODAY' , 'ANS_SCOOTER_TODAY'],
        ['Q_EXTEND_TIME', 'ANS_EXTEND_TIME'],
        ['Q_CHARGING', 'ANS_CHARGING'],
        ['Q_CANCEL_ORDER', 'ANS_CANCEL_ORDER'],
        ['Q_OUTSIDE_MCAD', 'ANS_OUTSIDE_MCAD']
        ])
    def test_how_mach(self):
        home_page = HomePage(driver)
        home_page.driver.go_to_site()
        home_page.driver.find_question_block()
        home_page.driver.check_answer_how_mush()




