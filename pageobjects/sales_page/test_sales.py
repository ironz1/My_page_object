from pytest_bdd import scenarios, given, when, then
from pageobjects.sales_page.actions import Sales
from pageobjects.login_page.actions import NopCommerce
scenarios('sales.feature')


@given("I am logged in")
def logged_in(base_url, selenium_driver):
    Sales(base_url, selenium_driver).open()
    NopCommerce(base_url, selenium_driver).click_login()


@when("I select Sales")
def select_sales(base_url, selenium_driver):
    Sales(base_url, selenium_driver).click_menu_sales()


@then("I can select gift card from side menu")
def click_side_menu(base_url, selenium_driver):
    Sales(base_url, selenium_driver).click_gift_cart()