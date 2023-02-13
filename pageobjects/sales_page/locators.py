from attrdict import AttrDict
from selenium.webdriver.common.by import By


class SalesPageLocators:
    """
    Class where are stored all locators from welcome page
    """
    locators = AttrDict(dict(
        gift_cart_on_panel=(
            By.XPATH, '//*[contains(@href, "GiftCard/List")]'),
        sales_icon=(
            By.XPATH, '//*[@class="nav-icon fas fa-shopping-cart"]'),
    ))
