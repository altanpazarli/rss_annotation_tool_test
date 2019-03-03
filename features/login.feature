Feature: Login

  Scenario: Successful login with correct credentials
    Given Registered user
    And User on homepage
    When fill form with correct credentials
    And submit the form
    Then User should see welcome message

  Scenario: Failed login due to incorrect username or password
    Given Registered user
    And User on homepage
    When fill form with incorrect credentials
    And submit the form
    Then User should see welcome message