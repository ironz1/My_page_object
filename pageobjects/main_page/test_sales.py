from pytest_bdd import scenarios, given, when, then
from pageobjects.main_page.actions import MainPage
from pageobjects.login_page.test_regular import login

scenarios('main.feature')


@given("I am logged in")
def logged_in(base_url, selenium):
    MainPage(base_url, selenium).open()
    login(base_url, selenium)


@when("I add task")
def add_task(base_url, selenium):
    MainPage(base_url, selenium).click_add_task()
    MainPage(base_url, selenium).enter_task_name()
    MainPage(base_url, selenium).enter_task_description()
    MainPage(base_url, selenium).click_add_task_submit_button()


@then("New task is added")
def click_side_menu(base_url, selenium):
    assert MainPage(base_url, selenium).is_task_on_list()
