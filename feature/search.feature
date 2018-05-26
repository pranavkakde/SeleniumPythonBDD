Feature: AutomationPracticeSearchOptions
    As a user I want to search on AutomationPractice.com
    @searchhome
    Scenario Outline: on search page search on <searchtext> and verify if <results> are displayed
        Given Search Text Box is visible
        When User enter <searchtext>
        Then show <results> on search page
        Examples: Search text
            | searchtext | results                 |
            | Shirt      | Showing 1 - 1 of 1 item |
    @filtercotton
    Scenario Outline: on Dresses page filter on cotton dresses and verify if <results> are displayed
        Given Dresses menu option is visible
        And User clicks on Dresses menu
        And Cotton option is visible
        When User selects Cotton option
        Then show filtered <results> on Dresses page
        Examples: Filter on Dresses
            | results                 |
            | Showing 1 - 1 of 1 items |