from pytest_bdd import scenarios, given, when, then
from pageobjects.login_page.login_page_actions import LoginPage


scenarios('regular.feature')

LOGIN = 'homkonektred@gmail.com'
PASSWORD = 'homeconnect1#'


@given("I enter Nopcommerce page")
def open_page(base_url, selenium):
    LoginPage(base_url, selenium).open()


@when("Login screen is displayed")
def is_login_page_displayed(base_url, selenium):
    assert LoginPage(base_url, selenium).is_page_title_displayed() == 'Todoist | A To-Do List to Organize Your Work & Life'


@then("I can log in")
def login(base_url, selenium):
    LoginPage(base_url, selenium).click_login()
    assert LoginPage(base_url, selenium).is_page_title_displayed() == 'Log in to Todoist'
    LoginPage(base_url, selenium).enter_email(email=LOGIN)
    LoginPage(base_url, selenium).enter_password(password=PASSWORD)
    LoginPage(base_url, selenium).start_login_button()
    assert LoginPage(base_url, selenium).is_todoist_app_loaded()



