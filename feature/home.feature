Feature: AutomationPractice
    As a user I want to browse to the AutomationPractice.com and search
    Scenario Outline: visit <browserpage> and check <browsertitle>
        When User visits "<browserpage>"
        Then it should have a title <browsertitle>
        Examples: Browser
            | browserpage                             | browsertitle |
            | http://automationpractice.com/index.php | My Store     |
