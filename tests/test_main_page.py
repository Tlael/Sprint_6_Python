import allure
import pytest
from selenium import webdriver
from data.data import DESCRIPTIONS
from pages.main_page import MainPage
from pages.urls import SCOOTER_URL


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @pytest.mark.parametrize('accord_number, expected_answer', [
        (1, DESCRIPTIONS[1]),
        (2, DESCRIPTIONS[2]),
        (3, DESCRIPTIONS[3]),
        (4, DESCRIPTIONS[4]),
        (5, DESCRIPTIONS[5]),
        (6, DESCRIPTIONS[6]),
        (7, DESCRIPTIONS[7]),
        (8, DESCRIPTIONS[8])
    ])
    @allure.title('Проверка аккордеона {accord_number}')
    def test_check_accordions(self, accord_number, expected_answer):
        self.driver.get(SCOOTER_URL)
        main_page = MainPage(self.driver)
        main_page.open_accordion(accord_number)
        actual_answer = main_page.get_answer_text(accord_number)
        assert actual_answer == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
