from pytest_bdd import scenarios, when, parsers, then

scenarios('../features/login.feature')


@when('I tap on the login button')
def _(driver):
    pass


@when(parsers.parse('enter the credentials "{user}", "{password}"'))
def _(driver, user, password):
    pass


@then(parsers.parse('the email validation error message "{expected_error_msg}" appears'))
def _(driver, expected_error_msg):
    pass


@then('I can login in my account successfully')
def _(driver):
    pass


