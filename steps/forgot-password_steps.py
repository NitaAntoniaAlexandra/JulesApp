from behave import *

@when('forgot_password: I set my email "{email}"')
def step_impl(context, email):
    context.forgot_password_page.set_email(email)

@when('forgot_password: I click on the send email button')
def step_impl(context):
    context.forgot_password_page.click_send_email_button()

@then('forgot_password: I verify that email validation message is correct')
def step_impl(context):
    context.forgot_password_page.verify_email_error_message()

