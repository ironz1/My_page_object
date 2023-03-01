from pytest_bdd import scenarios, given, when, then
from pageobjects.login_page.actions import NopCommerce


scenarios('regular.feature')

LOGIN = 'homkonektred@gmail.com'
PASSWORD = 'homeconnect1#'


@given("I enter Nopcommerce page")
def open_page(base_url):
    NopCommerce(base_url).open()


@when("Login screen is displayed")
def is_login_page_displayed(base_url):
    assert NopCommerce(base_url).is_page_title_displayed() == 'Todoist | A To-Do List to Organize Your Work & Life'


@then("I can log in")
def login(base_url):
    NopCommerce(base_url).click_login()
    assert NopCommerce(base_url).is_page_title_displayed() == 'Log in to Todoist'
    NopCommerce(base_url).enter_email(email=LOGIN)
    NopCommerce(base_url).enter_password(password=PASSWORD)
    NopCommerce(base_url).start_login_button()
    assert NopCommerce(base_url).is_todoist_app_loaded()



