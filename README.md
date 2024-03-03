# Selenium Automation Project - Target Online Shopping
# Overview
This Selenium automation project is designed to test the functionality of adding a product to the cart on the Target online shopping website. In the primary scenario, we will focus on searching for a specific product, adding the first search result to the cart, and verifying the successful addition of the product to the cart.

# Test Scenario
## Scenario: User can add a product to the cart on Target
Given Open Target main page: The test begins by navigating to the Target main page.

When Search for Stanley Cup: The automation script performs a search for the product "Stanley Cup" on the Target website.

Then Add to cart first result of product: The first search result (product) is selected, and the "Add to cart" action is executed.

And Verify product is added to the cart successfully: The script verifies that the selected product is successfully added to the cart by checking for relevant UI elements or messages.


