import allure
from selenium import webdriver
from pages.main_page import MainPage


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Проверка первого аккордеона')
    def test_click_accordion_1(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_accordion_1()

    @allure.title('Проверка второго аккордеона')
    def test_click_accordion_2(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_accordion_2()

    @allure.title('Проверка третьего аккордеона')
    def test_click_accordion_3(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_accordion_3()

    @allure.title('Проверка четвертого аккордеона')
    def test_click_accordion_4(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_accordion_4()

    @allure.title('Проверка пятого аккордеона')
    def test_click_accordion_5(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_accordion_5()

    @allure.title('Проверка шестого аккордеона')
    def test_click_accordion_6(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_accordion_6()

    @allure.title('Проверка седьмого аккордеона')
    def test_click_accordion_7(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_accordion_7()

    @allure.title('Проверка восьмого аккордеона')
    def test_click_accordion_8(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_accordion_8()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
