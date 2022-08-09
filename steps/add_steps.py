from behave import *


@when('add_page: I click on the property button')
def step_impl(context):
    context.add_page.click_property()
