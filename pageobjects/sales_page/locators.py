from attrdict import AttrDict
from selenium.webdriver.common.by import By


class LoginPageLocators:
    """
    Class where are stored all locators from welcome page
    """
    locators = AttrDict(dict(
        login_button=(
            By.XPATH, '//*[@type="submit"]'),
        sales_icon=(
            By.XPATH, '//*[@class="nav-icon fas fa-shopping-cart"]'),

    ))