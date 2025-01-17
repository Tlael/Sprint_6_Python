from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator)
        )

    def scroll_into_view_and_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_visible_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return element.text
