Feature: Add a product to cart on Target website

  Scenario: User can add a product to the cart on Target
    Given Open Target main page
    When Search for stanley cup
    Then Add to cart first result of product
    And Verify stanley cup is added to the cart successfully
