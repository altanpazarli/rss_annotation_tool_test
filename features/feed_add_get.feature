Feature: Adding Feed

    Scenario: User adds RSS feed
    Given the registered user logged in
    When the user clicks new feed button
    Then the user should see added RSS


    Scenario: User checks RSS feed
    Given the user on feeds page
    Then the user should be able to see feeds