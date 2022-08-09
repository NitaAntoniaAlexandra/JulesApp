from behave import *


@when('add_property_page: I set property`s "{name}"')
def step_impl(context, name):
    context.add_property_page.set_property_nickname(name)


@when('add_property_page: I click the no thanks button if it is displayed')
def step_impl(context, by,selector):
    context.add_property_page.click_if_present(by,selector)


@when('add_property_page: I click the continue button')
def step_impl(contxt):
    contxt.add_property_page.click_continue_button()


@when('add_property_page: I click the save button')
def step_impl(contxt):
    contxt.add_property_page.click_save_button()


@when('add_property_page: I click the finish button')
def step_impl(contxt):
    contxt.add_property_page.click_finish_button()


@then('add_property_page: the succes message is displayed')
def step_impl(context):
    context.add_property_page.verify_succes_message()
