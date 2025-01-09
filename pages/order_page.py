import allure
from pages.base_page import BasePage
from locators import OrderPageLocator

class OrderPage(BasePage):
    @allure.step('Ввод имени')
    def input_name(self, name: str):
        return self.find_element(OrderPageLocator.NAME_INPUT).send_keys(name)

    @allure.step('Ввод фамилии')
    def input_last_name(self, last_name: str):
        return self.find_element(OrderPageLocator.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        return self.find_element(OrderPageLocator.ADDRESS_INPUT).send_keys(address)

    @allure.step('Выбор станции метро')
    def choose_metro(self, metro_station: str):
        self.find_element(OrderPageLocator.METRO_STATION_INPUT).click()
        return self.find_element(OrderPageLocator.METRO_SELECTION(metro_station)).click()

    @allure.step('Ввод номера телефона')
    def input_phone_number(self, phone_number: str):
        return self.find_element(OrderPageLocator.PHONE_NUMBER_INPUT).send_keys(phone_number)

    @allure.step('Нажать "Далее"')
    def tap_next(self):
        return self.find_element(OrderPageLocator.NEXT_BUTTON).click()

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        return self.find_element(OrderPageLocator.DATE_INPUT).send_keys(date)

    @allure.step('Выбор срока аренды')
    def choose_rental_period(self, options=int):
        self.find_element(OrderPageLocator.RENTAL_PERIOD_INPUT).click()
        return self.find_elements(OrderPageLocator.RENTAL_PERIOD_LIST)[options].click()

    @allure.step('Выбор цвета самоката')
    def choose_color(self, options=int):
        return self.find_elements(OrderPageLocator.COLOR_INPUT)[options].click()

    @allure.step('Нажать "Заказать"')
    def tap_order(self):
        return self.find_element(OrderPageLocator.MIDDLE_ORDER_BUTTON).click()

    @allure.step('Подтвердить оформление заказа')
    def accept_order(self):
        return self.find_element(OrderPageLocator.ACCEPT_ORDER_BUTTON).click()

    @allure.step('Заполнить форму "Для кого самокат"')
    def fill_form_whom(self, set_user: dict):
        self.input_name(set_user['name'])
        self.input_last_name(set_user['surname'])
        self.input_address(set_user['address'])
        self.choose_metro(set_user['metro_station'])
        self.input_phone_number(set_user['phone_number'])

    @allure.step('Заполнить форму "Про аренду"')
    def fill_form_about_rent(self, set_user: dict):
        self.input_date(set_user['date'])
        self.choose_rental_period(set_user['rental_period'])
        for option in set_user['color']:
            self.choose_color(option)