Feature: User Creation

    Scenario: Invalid user creation
    Given the user is on the signup page
    When the user fills related forms with invalid data
    And the user clicks signup button
    Then the user should see enter valid username warning
    And the user should see password is too short warning

  Scenario: Successful user creation
    Given the user is on the signup page
    When the user fills related forms
    And the user clicks signup button
    Then the user should be redirected to feeds page
    And the user should see welcome message

  Scenario: Successful login
    Given the registered user on the login page
    When the user fills valid credentials
    And the user clicks login button
    Then the user should see my feeds button

  Scenario: Invalid login
    Given the registered user on the login page
    When the user fills invalid credentials
    And the user clicks login button
    Then the user should see wrong credentials warning

