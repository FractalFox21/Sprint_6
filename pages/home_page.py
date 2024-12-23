import locators


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://qa-scooter.praktikum-services.ru/'

    def go_to_site(self):
        self.driver.get(self.url)

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

    def find_question_block(self, question, answer):
        self.driver.find_element(locators.HomePageLocators.QUESTIONS_BLOCK)
        self.driver.find_element(question).click()




