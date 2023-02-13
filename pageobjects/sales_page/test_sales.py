from pytest_bdd import scenarios, given, when, then

scenarios('sales.feature')


@given("I am logged in")
def step_impl():
    pass


@when("I select Sales")
def step_impl():
    pass


@then("Side menu expands")
def step_impl():
    pass