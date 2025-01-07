import allure
from constants import Constants
from pages.home_page import HomePage

class TestHomePage:
    @allure.title('Проверка работы кнопки "Заказать" вверху страницы ')
    @allure.description('Нажимаем кнопку "Заказать" и сравниваем текущий URL с ожидаемым. \
    Должна открыться страница оформления заказа.')
    def test_tap_header_order_button_open_order_page(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie()
        home_page.click_header_order_button()
        assert home_page.current_url() == Constants.URL_ORDER_PAGE

    @allure.title('Проверка работы кнопки "Заказать" внизу страницы')
    @allure.description('Нажимаем кнопку "Заказать", и сравниваем текущий URL с ожидаемым. \
    Должна открыться страница оформления заказа.')
    def test_tap_finish_order_button_open_order_page(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie()
        home_page.click_bottom_order_button()
        assert home_page.current_url() == Constants.URL_ORDER_PAGE

    @allure.title('Переход на страницу "ДЗЕН" по нажатию на логотип "Яндекс"')
    @allure.description('Нажимаем на логотип "Яндекс" вверху страницы, переходим а открывшуюся вкладку, \
    сравниваем текущий URL с ожидаемым. Должна быть открыта страница "ДЗЕН"')
    def test_tap_yandex_logo_open_yandex_page(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie()
        home_page.click_yandex_logo()
        home_page.switch_window(1)
        home_page.page_load()
        current_url = home_page.current_url()
        assert Constants.URL_DZEN_PAGE in current_url

    @allure.title('Переход на главную страницу Самоката при нажатии на лого Самоката')
    @allure.description('Переходим на страницу оформления заказа. Находясь на странице оформления заказа нажимаем на логотип "Самокат". \
    Сравниваем текущий URL c ожидаемым. Должна быть открыта домашняя страница.')
    def test_click_scooter_logo_open_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site(Constants.URL_ORDER_PAGE)
        home_page.click_scooter_logo()
        current_url = driver.current_url
        assert Constants.URL_HOME_PAGE in current_url
