Feature: User Creation

  Scenario: Successful user creation
    Given the user is on the signup page
    When the user fills related forms
    And the user clicks signup button
    Then the user should be redirected to feeds page
    And the user should see welcome message


  Scenario: Successful login
    Given the registered user on the login page
    When the user fills username and password
    Then the user should see my feeds button