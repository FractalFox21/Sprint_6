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


    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                message=f"Элемент {locator} не найден")

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator),
                message=f"Элементы {locator} не найдены")

    @allure.step('Принять куки')
    def click_cookie(self):
        return self.find_element(BasePageLocators.COOKIE_ACCEPT_BUTTON).click()

    @allure.step('Получить текущий url')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Нажать на логотип "Самокат"')
    def click_scooter_logo(self):
        return self.find_element(BasePageLocators.SCOOTER_LOGO).click()

    @allure.step('Нажать на логотип "Яндекс"')
    def click_yandex_logo(self):
        return self.find_element(BasePageLocators.YANDEX_LOGO).click()

    @allure.step('Переключиться на открывшуюся страницу')
    def switch_window(self, window_number: int=1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    def page_load(self):
        return WebDriverWait(self.driver, 10).until_not(EC.url_to_be('about:blank'))
