import allure
from selenium import webdriver
from pages.order_page import OrderPage


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Оформление заказа через кнопку в хедере')
    def test_order_with_button_in_header(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrderPage(self.driver)
        order_page.click_button_in_header()
        order_page.get_order('Иван', 'Иванов', 'Ленина 5', 'Улица 1905 года', '89051112233', '18.01.2025',
                             'Тестовый комментарий')

    @allure.title('Оформление заказа через кнопку на сайте')
    def test_order_with_button_in_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrderPage(self.driver)
        order_page.click_button_in_page()
        order_page.get_order('Петр', 'Петров', 'Тимирязева 10', 'Беговая', '89163334455', '23.01.2025',
                             'Ещё один тестовый комментарий')

    @allure.title('Проверка url при клике по логотипу самоката')
    def test_click_scooter(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrderPage(self.driver)
        order_page.click_logo_scooter()

    @allure.title('Проверка url при клике по логотипу yandex')
    def test_click_yandex(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrderPage(self.driver)
        order_page.click_logo_yandex()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
