from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):

    def open_main(self):
        self.open('https://www.target.com/')
