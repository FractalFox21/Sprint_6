import allure
from pages.base_page import BasePage
from locators import HomePageLocators

class HomePage(BasePage):

    @allure.step('Нажать кнопку "Заказать" в верхней части страницы')
    def click_header_order_button(self):
        return self.find_element(HomePageLocators.HEADER_ORDER_BUTTON).click()

    @allure.step('Нажать кнопку "Заказать" в нижней части страницы')
    def click_bottom_order_button(self):
        return self.find_element(HomePageLocators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Нажать на вопрос')
    def click_faq_question(self, question_number):
        elem = self.find_elements(HomePageLocators.FAQ_BUTTON)
        return elem[question_number].click()
