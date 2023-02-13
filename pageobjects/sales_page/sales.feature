Feature: Sales page

  @automated
  Scenario: Select Sales
    Given I am logged in
    When I select Sales
    Then I can select gift card from side menu
