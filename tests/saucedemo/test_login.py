import pytest
from pages.saucedemo.saucedemo_page import SaucedemoPage
from constants import login_error_constants


class TestSaucedemo:

    STATUS_SUCCESS = "Success"
    STATUS_LOCKED = 'Locked'

    @pytest.mark.parametrize("user, desired_screen", [
        (SaucedemoPage.valid_user(), STATUS_SUCCESS),
        (SaucedemoPage.locked_user(), STATUS_LOCKED),
    ])
    def test_login(self, page, user, desired_screen):
        saucedemo = SaucedemoPage(page).login_page
        saucedemo.go()
        saucedemo.enter_username(user["user"])
        saucedemo.enter_password(user["password"])
        saucedemo.click_login()

        def assert_success():
            assert saucedemo.get_current_url().endswith("/inventory.html")

        def assert_locked():
            assert saucedemo.get_login_error_text() == login_error_constants.user_locked

        assertions = {
            self.STATUS_SUCCESS: assert_success,
            self.STATUS_LOCKED: assert_locked
        }

        assertions[desired_screen]()
