from pageobjects.common_base.base_page import BasePage
from pageobjects.login_page.locators import LoginPageLocators


class NopCommerce(BasePage):

    def click_login(self):
        self.click(LoginPageLocators.locators.login_button)


