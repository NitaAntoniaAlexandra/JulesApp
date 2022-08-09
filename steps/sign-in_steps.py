from behave import *

# given!, when!, and, but, then! - sintaxa gherkin
# given - seteaza situatia initiala
# when - pasii din test
# then - verificarea din test


@given('sign_in: I am a user on Jules signin page')
def step_impl(context):
    context.sign_in_page.navigate_to_sigin_page()


@when('sign_in: I set my email "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)


@when('sign_in: I set my password "{password}"')
def step_impl(context, password):
    context.sign_in_page.set_password(password)


@when('sign_in: I click on login button')
def step_impl(context):
    context.sign_in_page.click_login_button()

@when('sign_in: I click on forgot_password_link')
def step_impl(context):
    context.sign_in_page.click_forgot_password_link()
