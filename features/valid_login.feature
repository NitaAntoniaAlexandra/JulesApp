Feature: Jules valid_login tests

    Background:
      #se ruleaza inainte de fiecare test, se pun in general given-urile
      Given sign_in: I am a user on Jules signin page

    @jules2
    Scenario: Valid login
      When sign_in: I set my email "email"
      When sign_in: I set my password "password"
      When sign_in: I click on login button
      Then search_all: I am a user on search page

    @jules2
    Scenario Outline: Valid login with table data
      When sign_in: I set my email "<email>"
      When sign_in: I set my password "<password>"
      When sign_in: I click on login button
      Then search_all: I am a user on search page

      Examples:
        | email                      | password   |
        | tarzioru.antonia@gmail.com | Test110620*|

