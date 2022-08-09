from behave import *


@when('menu_page: I click on the add button')
def step_impl(context):
    context.menu_page.click_add_button()


@when('menu_page: I click on the library button')
def step_impl(context):
    context.menu_page.click_library_button()


@when('menu_page: I click on the connections button')
def step_impl(context):
    context.menu_page.click_connections_button()


@when('menu_page: I click on the search button')
def step_impl(context):
    context.menu_page.click_search_button()
