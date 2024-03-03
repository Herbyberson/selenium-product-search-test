from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_element_visible(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} is not clickable'
        )

    def wait_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        )

    def wait_element_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        ).click()

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            f"Expected '{expected_text}' but got '{actual_text}'"

    def verify_partial_text(self, expected_text, *locator):
        expected_text = expected_text.lower()
        actual_text = self.find_element(*locator).text
        actual_text = actual_text.lower()
        assert expected_text in actual_text, \
            f"Expected {expected_text} not in '{actual_text}'"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, \
            f"Expected '{expected_url}' but got '{actual_url}'"

    def verify_partial_url(self, expected_partial_url):
        # actual_url = self.driver.current_url
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f"Expected '{expected_partial_url}' not found")
