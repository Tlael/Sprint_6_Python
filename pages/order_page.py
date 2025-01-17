import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators_order_page import *
from pages.urls import *
from data.data import MESSAGE_ORDER


class OrderPage(BasePage):

    @allure.step('Кликаем по кнопке Заказать в шапке')
    def click_button_in_header(self):
        self.find_element(BUTTON_ORDER_IN_HEADER).click()

    @allure.step('Кликаем по кнопке Заказать на странице')
    def click_button_in_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(BUTTON_ORDER_IN_PAGE))
        self.scroll_into_view_and_click(BUTTON_ORDER_IN_PAGE)

    @allure.step('Заполняем поля заявки')
    def get_order(self, name, surname, address, subway, phone, time, comment):
        self.find_element(FIELD_NAME).send_keys(name)
        self.find_element(FIELD_SURNAME).send_keys(surname)
        self.find_element(FIELD_ADDRESS).send_keys(address)
        self.find_element(FIELD_SUBWAY).send_keys(subway)
        self.find_element(LIST_SUBWAY).click()
        self.find_element(FIELD_PHONE).send_keys(phone)
        self.find_element(BUTTON_NEXT).click()

        self.find_element(FIELD_TIME).send_keys(time)
        self.find_element(CALENDAR).click()
        self.find_element(DROPDOWN_RENTS).click()
        self.find_element(TIME_RENTS).click()
        self.find_element(CHECKBOX_COLOR_BLACK).click()
        self.find_element(FIELD_COMMENT).send_keys(comment)
        self.find_element(BUTTON_ORDER).click()

        self.find_element(BUTTON_YES).click()

        order = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(VIEW_STATUS))
        description = order.text
        assert description == MESSAGE_ORDER

    @allure.step('Кликаем по логотипу самокат')
    def click_logo_scooter(self):
        self.find_element(LOGO_SCOOTER).click()
        assert self.driver.current_url == SCOOTER_URL

    @allure.step('Кликаем по логотипу Яндекс')
    def click_logo_yandex(self):
        self.find_element(LOGO_YANDEX).click()

        # Переключение на новое окно
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # Ждем, пока загрузится новая страница
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(YANDEX_URL))

        # Проверка URL
        assert self.driver.current_url == YANDEX_URL
