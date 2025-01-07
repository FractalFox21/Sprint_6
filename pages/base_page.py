import allure
from constants import Constants
from locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на сайт')
    @allure.description('Если URL сайта не задан, откроет домашнюю страницу')
    def go_to_site(self, url=None):
        if url is None:
            url = Constants.URL_HOME_PAGE
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                message=f"Элемент {locator} не найден")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                message=f"Элементы {locator} не найдены")

    @allure.step('Принять куки')
    def click_cookie(self):
        return self.find_element(BasePageLocators.COOKIE_ACCEPT_BUTTON).click()






