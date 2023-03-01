from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """BasePage is a parent class for each page class then this way of implementation allow us
    to use his self attributes inside typical page."""

    def __init__(self, base_url, selenium):
        self.base_url = base_url
        self.selenium = selenium
        self.wait = WebDriverWait(driver=selenium, timeout=2)

    def open(self):
        self.selenium.get(self.base_url)
        self.selenium.maximize_window()

    def click(self, locator, timeout=6):
        element = self.find_element(locator, timeout=timeout)
        element.click()

    def find_element(self, locator, timeout=15):
        self.selenium.implicitly_wait(timeout)
        return self.selenium.find_element(*locator)

    def find_elements(self, locator):
        return self.selenium.find_elements(*locator)

    def take_screenshot(self):
        self.selenium.save_screenshot('screenshots/screen.png')

    def is_page_title_displayed(self):
        return self.selenium.title

    def enter_text(self, locator, string):
        element = self.find_element(locator)
        element.send_keys(string)

    def is_element_displayed(self, locator):
        element = self.find_element(locator)
        return element.is_displayed()
