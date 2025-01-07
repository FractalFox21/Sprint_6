
class Constants:
    URL_HOME_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    URL_ORDER_PAGE = f'{URL_HOME_PAGE}order'
    URL_DZEN_PAGE = 'dzen.ru'


class ExpectedAnswer:
    answer_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    answer_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    answer_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    answer_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    answer_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    answer_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    answer_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    answer_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

class SetUser:
    set_user = {
        'user_1': {
            'name': 'Иван',
            'surname': 'Иванов',
            'address': 'Москва',
            'metro_station': 'Бибирево',
            'phone_number': '88888888888',
            'date': '30.01.2025',
            'rental_period': 0,
            'color': [0],
        },
        'user_2': {
            'name': 'Пётр',
            'surname': 'Петров',
            'address': 'Москва, улица Ленина',
            'metro_station': 'Алтуфьево',
            'phone_number': '99999999999',
            'date': '22.02.2025',
            'rental_period': 0,
            'color': [1],
        }
    }
