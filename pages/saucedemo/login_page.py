from pages.base_page import BasePage


class LoginPage(BasePage):

    def go(self):
        self.navigate("https://www.saucedemo.com/")

    def get_login_error_text(self):
        return self.get_text('h3[data-test="error"]')

    def enter_username(self, user):
        self.fill_text_field('input[data-test="username"]', user)

    def enter_password(self, password):
        self.fill_text_field('input[data-test="password"]', password)

    def click_login(self):
        self.click_element('input[data-test="login-button"]')
