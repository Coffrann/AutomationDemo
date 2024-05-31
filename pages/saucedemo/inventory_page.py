from pages.base_page import BasePage


class InventoryPage(BasePage):
    button_shopping_cart = BasePage.data_test("shopping-cart-link")
    button_hamburger_icon = "#react-burger-menu-btn"
    text_inventory_section_title = "div.app_logo"
    text_products_heading = BasePage.data_test("title")
    text_footer_copyright = BasePage.data_test("footer-copy")
    dropdown_sort = BasePage.data_test("product-sort-container")

    def get_inventory_text(self):
        return self.get_text(self.text_inventory_section_title)

    def click_hamburger_icon(self):
        self.click_element(self.button_hamburger_icon)

    def click_shopping_cart(self):
        self.click_element(self.button_shopping_cart)

    def get_shopping_cart_status(self):
        return self.is_element_visible(self.button_shopping_cart)

    def get_products_heading_text(self):
        return self.get_text(self.text_products_heading)

    def get_copyright_text(self):
        return self.get_text(self.text_footer_copyright)

    def click_sort_dropdown(self):
        self.click_element(self.dropdown_sort)

    def select_sort_dropdown_option_by_value(self, value):
        self.select_option_by_value(self.dropdown_sort, value)

    def get_sort_dropdown_text(self):
        return self.get_selected_option(self.dropdown_sort)
