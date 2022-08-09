Feature: Jules add property tests

    Background:

      Given sign_in: I am a user on Jules signin page

    @jules22
    Scenario Outline: Valid property add with table data
      When sign_in: I set my email "<email>"
      When sign_in: I set my password "<password>"
      When sign_in: I click on login button
      When menu_page: I click on the add button
      When add_page: I click on the property button
      When add_property_page: I set property`s "<name>"
      When add_property_page: I click the continue button
      When add_property_page: I click the no thanks button if it is displayed
      #When add_property_page: I click the save button
      #Then add_property_page: the success message is displayed
      Examples:
        | email                      | password   |name|
        | tarzioru.antonia@gmail.com | Test110620*|1234|