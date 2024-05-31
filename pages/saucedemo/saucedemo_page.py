import pytest
from pages.base_page import BasePage
from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage


class SaucedemoPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)

    @staticmethod
    def valid_user():
        return {"user": "standard_user", "password": "secret_sauce"}

    @staticmethod
    def locked_user():
        return {"user": "locked_out_user", "password": "secret_sauce"}


@pytest.fixture
def inventory_page(page):
    saucedemo = SaucedemoPage(page).login_page
    saucedemo.go()
    saucedemo.enter_username(SaucedemoPage.valid_user()["user"])
    saucedemo.enter_password(SaucedemoPage.valid_user()["password"])
    saucedemo.click_login()
    return SaucedemoPage(page).inventory_page
