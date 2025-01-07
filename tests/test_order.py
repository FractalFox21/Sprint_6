import pytest
import allure
from constants import Constants
from locators import OrderPageLocator
from constants import SetUser
from pages.order_page import OrderPage
from pages.home_page import HomePage

class TestOrder:
    @allure.title('При создании заказа появляется поп-ап с сообщением об успешном оформлении заказа')
    @allure.description('Переходим к созданию заказа, вводим данные тестовых пользователей, \
    Ищем на странице уведомление об успешном оформлении заказа и проверяем, что его текст == "Заказ оформлен"')

    @pytest.mark.parametrize('user_set', ['user_1', 'user_2'])
    def test_placing_order_by_using_top_order_button_positive_result(self, driver, user_set):
        order_page = OrderPage(driver)
        order_page.go_to_site(Constants.URL_ORDER_PAGE)
        home_page = HomePage(driver)
        home_page.click_cookie()
        order_page.fill_form_whom(SetUser.set[user_set])
        order_page.tap_next()
        order_page.fill_form_about_rent(SetUser.set[user_set])
        order_page.tap_order()
        order_page.accept_order()
        status = driver.find_element(*OrderPageLocator.ORDER_STATUS)
        assert 'Заказ оформлен' in status.text
