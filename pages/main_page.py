from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators_main_page import *


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_accordion_1(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*ACCORDION_1))
        self.driver.find_element(*ACCORDION_1).click()
        actual = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ANSWER_1))
        description = actual.text
        assert description == DESCRIPTION_1

    def click_accordion_2(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*ACCORDION_2))
        self.driver.find_element(*ACCORDION_2).click()
        actual = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ANSWER_2))
        description = actual.text
        assert description == DESCRIPTION_2

    def click_accordion_3(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*ACCORDION_3))
        self.driver.find_element(*ACCORDION_3).click()
        actual = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ANSWER_3))
        description = actual.text
        assert description == DESCRIPTION_3

    def click_accordion_4(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*ACCORDION_4))
        self.driver.find_element(*ACCORDION_4).click()
        actual = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ANSWER_4))
        description = actual.text
        assert description == DESCRIPTION_4

    def click_accordion_5(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*ACCORDION_5))
        self.driver.find_element(*ACCORDION_5).click()
        actual = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ANSWER_5))
        description = actual.text
        assert description == DESCRIPTION_5

    def click_accordion_6(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*ACCORDION_6))
        self.driver.find_element(*ACCORDION_6).click()
        actual = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ANSWER_6))
        description = actual.text
        assert description == DESCRIPTION_6

    def click_accordion_7(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*ACCORDION_7))
        self.driver.find_element(*ACCORDION_7).click()
        actual = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ANSWER_7))
        description = actual.text
        assert description == DESCRIPTION_7

    def click_accordion_8(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*ACCORDION_8))
        self.driver.find_element(*ACCORDION_8).click()
        actual = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ANSWER_8))
        description = actual.text
        assert description == DESCRIPTION_8
