from behave import *


@when('search_all: I fill the search field and click Enter')
def step_impl(context):
    context.search_all_page.fill_search_field_click_enter()


@when('search_all: I click filter button')
def step_impl(context):
    context.search_all_page.click_filter_button()


@when('search_all: I click record button')
def step_impl(context):
    context.search_all_page.click_record_button()


@when('search_all : I click testing jules app real estate section')
def step_impl(context):
    context.search_all_page.click_testing_jules_app_real_estate()


@then('search_all: I am a user on search page')
def step_impl(context):
    context.search_all_page.verify_correct_page()
