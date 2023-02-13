Feature: Login to system

  @automated
  Scenario: Open nopCommerce
    Given I enter Nopcommerce page
    When Login screen is displayed
    Then I can log in
