import allure
import pytest
from selenium import webdriver

from pages.order_page import OrderPage
from resources.urls import SCOOTER_URL


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize(
        'name, surname, address, subway, phone, time, comment', [
            ['Иван', 'Иванов', 'Ленина 5', 'Улица 1905 года', '89051112233', '18.01.2025',
             'Тестовый комментарий'],
            ['Петр', 'Петров', 'Тимирязева 10', 'Беговая', '89163334455', '19.02.2025',
             'Ещё один тестовый комментарий']
        ]
    )
    @allure.title('Оформление заказа через кнопку в хедере')
    def test_order_with_button_in_header(self, name, surname, address, subway, phone, time, comment):
        self.driver.get(SCOOTER_URL)
        order_page = OrderPage(self.driver)
        order_page.click_button_in_header()
        order_page.get_order(name, surname, address, subway, phone, time, comment)

    @pytest.mark.parametrize(
        'name, surname, address, subway, phone, time, comment', [
            ['Иван', 'Иванов', 'Ленина 5', 'Улица 1905 года', '89051112233', '18.01.2025',
             'Тестовый комментарий'],
            ['Петр', 'Петров', 'Тимирязева 10', 'Беговая', '89163334455', '19.02.2025',
             'Ещё один тестовый комментарий']
        ]
    )
    @allure.title('Оформление заказа через кнопку на сайте')
    def test_order_with_button_in_page(self, name, surname, address, subway, phone, time, comment):
        self.driver.get(SCOOTER_URL)
        order_page = OrderPage(self.driver)
        order_page.click_button_in_page()
        order_page.get_order(name, surname, address, subway, phone, time, comment)

    @allure.title('Проверка url при клике по логотипу самоката')
    def test_click_scooter(self):
        self.driver.get(SCOOTER_URL)
        order_page = OrderPage(self.driver)
        order_page.click_logo_scooter()

    @allure.title('Проверка url при клике по логотипу yandex')
    def test_click_yandex(self):
        self.driver.get(SCOOTER_URL)
        order_page = OrderPage(self.driver)
        order_page.click_logo_yandex()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
