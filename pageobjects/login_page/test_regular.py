from pytest_bdd import scenarios, given, when, then
from pageobjects.login_page.actions import NopCommerce


scenarios('regular.feature')


@given("I enter Nopcommerce page")
def open_page(base_url):
    NopCommerce(base_url).open()


@when("Login screen is displayed")
def is_login_page_displayed(base_url):
    assert NopCommerce(base_url).is_page_title_displayed() == 'Your store. Login'


@then("I can log in")
def step_impl(base_url):
    NopCommerce(base_url).click_login()
    assert NopCommerce(base_url).is_page_title_displayed() == 'Dashboard / nopCommerce administration'



