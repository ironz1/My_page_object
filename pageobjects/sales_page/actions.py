from pageobjects.common_base.base_page import BasePage
from pageobjects.sales_page.locators import SalesPageLocators


class Sales(BasePage):

    def click_menu_sales(self):
        self.click(SalesPageLocators.locators.sales_icon)

    def click_gift_cart(self):
        self.click(SalesPageLocators.locators.gift_cart_on_panel)


