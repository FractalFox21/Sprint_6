from selenium.webdriver.common.by import By


class HomePageLocators():
    TOP_ORDER_BUTTON = (By.CSS_SELECTOR, "button.Order_Button__1Lkhg")
    ORDER_BUTTON_IN_MANUAL = (By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm > button")


    QUESTIONS_BLOCK = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")
    Q_HOW_MUCH = (By.XPATH, "//div[@id='accordion__panel-8']")
    ANS_HOW_MUCH = (By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру')]")
    Q_SOME_SCOOTERS = (By.XPATH, "//div[@id='accordion__heading-9']")
    ANS_SOME_SCOOTERS = (By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат.')]")
    Q_RENTAL_TIME = (By.XPATH, "//div[@id='accordion__heading-10']")
    ANS__RENTAL_TIME = (By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая.')]")
    Q_SCOOTER_TODAY = (By.XPATH, "//div[@id='accordion__heading-11']")
    ANS_SCOOTER_TODAY = (By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня.')]")
    Q_EXTEND_TIME = (By.XPATH, "//div[@id='accordion__heading-12']")
    ANS_EXTEND_TIME = (By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное')]")
    Q_CHARGING = (By.XPATH, "//div[@id='accordion__heading-13']")
    ANS_CHARGING = (By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой.')]")
    Q_CANCEL_ORDER = (By.XPATH, "//div[@id='accordion__heading-14']")
    ANS_CANCEL_ORDER = (By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли.')]")
    Q_OUTSIDE_MCAD = (By.XPATH, "//div[@id='accordion__heading-15']")
    ANS_OUTSIDE_MCAD = (By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов!')]")