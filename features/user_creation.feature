Feature: User Creation

  Scenario: Successful user creation
    Given valid username and password
    And user on signup page
    When user fill related forms
    And click signup button
    Then user should see welcome message

  Scenario: Unsuccessful user creation
    Given invalid username and password
    And user on signup page
    When user fill related forms
    And click signup button
    Then user should see error message

  Scenario: Unsuccessful user creation
    Given same username and password
    And user on signup page
    When user fill related forms
    And click signup button
    Then user should see error message