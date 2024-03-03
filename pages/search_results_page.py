from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_ADD_TO_CART_BUTTON = (By.XPATH, "//div[@style='display: flex;']//button[@type='button']")
    VIEW_CART_PAGE = (By.XPATH, "//a[@href='/cart']")

    def click_add_to_cart_button(self):
        self.wait_element_clickable_click(*self.ADD_TO_CART_BUTTON)
        sleep(6)

    def click_add_to_cart_side_nav(self):
        # self.wait_element_clickable(*self.SIDE_NAV_ADD_TO_CART_BUTTON)
        # self.wait_element_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BUTTON)
        self.click(*self.SIDE_NAV_ADD_TO_CART_BUTTON)

    def view_cart_page(self):
        self.wait_element_clickable_click(*self.VIEW_CART_PAGE)
        sleep(6)
