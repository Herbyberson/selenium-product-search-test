from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='shippingButton']")
    VIEW_CART_PAGE = (By.XPATH, "//a[@href='/cart']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)

    def click_search_button(self):
        self.wait_element_clickable_click(*self.SEARCH_ICON)
        sleep(6)
