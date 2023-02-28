from attrdict import AttrDict
from selenium.webdriver.common.by import By


class LoginPageLocators:
    """
    Class where are stored all locators from welcome page
    """
    locators = AttrDict(dict(
        login_button=(
            By.XPATH, '//*[@href="/auth/login"]'),
        email_field=(
            By.ID, 'element-0'),
        password_field=(
            By.ID, 'element-3'),
        start_login_button=(
            By.XPATH, '//*[@data-gtm-id="start-email-login"]'),
        app_loaded=(
            By.ID, 'app_holder')
    ))
