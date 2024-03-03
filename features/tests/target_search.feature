# Created by 12396 at 3/2/2024
Feature: Add a product to cart on Target website
  # Enter feature description here

  Scenario: User can add a product to the cart on Target
    Given Open Target main page
    When Search for Tea
    Then Add to cart first result of product
    And Verify Tea is added to the cart successfully


    # Enter steps here