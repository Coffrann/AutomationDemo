import pytest
from pages.base_page import BasePage
from pages.saucedemo.login_page import LoginPage


class SaucedemoPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.login_page = LoginPage(page)

    @staticmethod
    def valid_user():
        return {"user": "standard_user", "password": "secret_sauce"}

    @staticmethod
    def locked_user():
        return {"user": "locked_out_user", "password": "secret_sauce"}
