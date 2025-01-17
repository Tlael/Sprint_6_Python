import allure

from pages.base_page import BasePage
from pages.locators_main_page import *


class MainPage(BasePage):
    ACCORDIONS = {
        1: ACCORDION_1,
        2: ACCORDION_2,
        3: ACCORDION_3,
        4: ACCORDION_4,
        5: ACCORDION_5,
        6: ACCORDION_6,
        7: ACCORDION_7,
        8: ACCORDION_8
    }

    ANSWERS = {
        1: ANSWER_1,
        2: ANSWER_2,
        3: ANSWER_3,
        4: ANSWER_4,
        5: ANSWER_5,
        6: ANSWER_6,
        7: ANSWER_7,
        8: ANSWER_8
    }

    @allure.step('Открываем аккордион {accord_number}')
    def open_accordion(self, accord_number):
        """Открывает указанный аккорд."""
        accordion_locator = self.ACCORDIONS[accord_number]
        self.scroll_into_view_and_click(accordion_locator)

    @allure.step('Получаем ответ аккордеона {accord_number}')
    def get_answer_text(self, accord_number):
        """Возвращает текст ответа указанного аккорда."""
        answer_locator = self.ANSWERS[accord_number]
        return self.get_visible_element_text(answer_locator)