import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators_order_page import *
from pages.urls import *


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def click_button_in_header(self):
        self.driver.find_element(*BUTTON_ORDER_IN_HEADER).click()

    def click_button_in_page(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*BUTTON_ORDER_IN_PAGE))
        self.driver.find_element(*BUTTON_ORDER_IN_PAGE).click()

    @pytest.mark.parametrize(
        'name, surname, address, subway, phone, time, comment', [
            ['Иван', 'Иванов', 'Ленина 5', 'Улица 1905 года', '89051112233', '18.01.2025',
             'Тестовый комментарий'],
            ['Петр', 'Петров', 'Тимирязева 10', 'Беговая', '89163334455', '19.02.2025',
             'Ещё один тестовый комментарий']
        ]
    )
    def get_order(self, name, surname, address, subway, phone, time, comment):
        self.driver.find_element(*FIELD_NAME).send_keys(name)
        self.driver.find_element(*FIELD_SURNAME).send_keys(surname)
        self.driver.find_element(*FIELD_ADDRESS).send_keys(address)
        self.driver.find_element(*FIELD_SUBWAY).send_keys(subway)
        self.driver.find_element(*LIST_SUBWAY).click()
        self.driver.find_element(*FIELD_PHONE).send_keys(phone)
        self.driver.find_element(*BUTTON_NEXT).click()

        self.driver.find_element(*FIELD_TIME).send_keys(time)
        self.driver.find_element(*CALENDAR).click()
        self.driver.find_element(*DROPDOWN_RENTS).click()
        self.driver.find_element(*TIME_RENTS).click()
        self.driver.find_element(*CHECKBOX_COLOR_BLACK).click()
        self.driver.find_element(*FIELD_COMMENT).send_keys(comment)
        self.driver.find_element(*BUTTON_ORDER).click()

        self.driver.find_element(*BUTTON_YES).click()

        order = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(VIEW_STATUS))
        description = order.text
        assert description == MESSAGE_ORDER

    def click_logo_scooter(self):
        self.driver.find_element(*LOGO_SCOOTER).click()
        assert self.driver.current_url == SCOOTER_URL

    def click_logo_yandex(self):
        self.driver.find_element(*LOGO_YANDEX).click()

        # Переключение на новое окно
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # Ждем, пока загрузится новая страница
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(YANDEX_URL))

        # Проверка URL
        assert self.driver.current_url == YANDEX_URL
