from behave import given, when, then


@given('Open Target main page')
def open_target_main(context):
    context.application.main_page.open_main()


@when('Search for {product}')
def search(context, product):
    context.application.header.search_product(product)
    context.application.header.click_search_button()


@then('Add to cart first result of product')
def add_to_cart_first_result(context):
    context.application.search_results_page.click_add_to_cart_button()
    context.application.search_results_page.click_add_to_cart_side_nav()
    context.application.search_results_page.view_cart_page()


@then('Verify {product} is added to the cart successfully')
def verify_cart_item(context, product):
    context.application.cart_page.verify_cart_item(product)
