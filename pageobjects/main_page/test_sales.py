from pytest_bdd import scenarios, given, when, then
from pageobjects.main_page.actions import MainPage
from pageobjects.login_page.test_regular import login

scenarios('main.feature')


@given("I am logged in")
def logged_in(base_url):
    MainPage(base_url).open()
    login(base_url)


@when("I add task")
def add_task(base_url):
    MainPage(base_url).click_add_task()
    MainPage(base_url).enter_task_name()
    MainPage(base_url).enter_task_description()
    MainPage(base_url).click_add_task_submit_button()


@then("New task is added")
def click_side_menu(base_url):
    assert MainPage(base_url).is_task_on_list()
