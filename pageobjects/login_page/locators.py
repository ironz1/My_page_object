from attrdict import AttrDict
from selenium.webdriver.common.by import By


class LoginPageLocators:
    """
    Class where are stored all locators from welcome page
    """
    locators = AttrDict(dict(
        login_button=(
            By.XPATH, '//*[@type="submit"]'),
        accreditation=(
            By.XPATH, '//*[@data-test-id="acc"]'),
        burger_button=(
            By.XPATH, '//*[@id="header-mega-menu"]/button'),

    ))
