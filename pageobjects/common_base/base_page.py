# from conftest import selenium
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """BasePage is a parent class for each page class then this way of implementation allow us
    to use his self attributes inside typical page."""
    # selenium = selenium()

    def __init__(self, base_url, selenium_driver):
        self.base_url = base_url
        self.selenium_driver = selenium_driver
        self.wait = WebDriverWait(driver=selenium_driver, timeout=2)

    def open(self):
        self.selenium_driver.get(self.base_url)
        self.selenium_driver.maximize_window()

    def click(self, locator, timeout=6):
        element = self.find_element(locator, timeout=timeout)
        element.click()

    def find_element(self, locator, timeout=6):
        self.selenium_driver.implicitly_wait(timeout)
        return self.selenium_driver.find_element(*locator)

    def find_elements(self, locator):
        return self.selenium_driver.find_elements(*locator)

    def take_screenshot(self):
        self.selenium_driver.save_screenshot('screenshots/screen.png')

    def is_page_title_displayed(self):
        return self.selenium_driver.title
