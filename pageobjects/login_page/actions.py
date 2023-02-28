from pageobjects.common_base.base_page import BasePage
from pageobjects.login_page.locators import LoginPageLocators


class NopCommerce(BasePage):

    def click_login(self):
        self.click(LoginPageLocators.locators.login_button)

    def enter_email(self, email):
        self.enter_text(LoginPageLocators.locators.email_field, email)

    def enter_password(self, password):
        self.enter_text(LoginPageLocators.locators.password_field, password)

    def start_login_button(self):
        self.click(LoginPageLocators.locators.start_login_button)

    def is_todoist_app_loaded(self):
        return self.find_element(LoginPageLocators.locators.app_loaded)

