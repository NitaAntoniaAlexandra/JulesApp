Feature: Jules editing_properties tests

    Background:

      Given sign_in: I am a user on Jules signin page

    @jules221
    Scenario Outline: Valid login with table data
      When sign_in: I set my email "<email>"
      When sign_in: I set my password "<password>"
      When sign_in: I click on login button
      When menu_page: I click on the add button
      When add_page: I click on the property button


      Examples:
        | email                      | password   |
        | tarzioru.antonia@gmail.com | Test110620*|