from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class CartPage(Page):

    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_item(self, product):
        self.verify_partial_texts(product, *self.PRODUCT_DESCRIPTION)
