from pages.saucedemo.saucedemo_page import inventory_page
from constants import inventory_constants


class TestSaucedemoInventoryConstants:

    def test_inventory_main_nav_title(self, inventory_page):
        assert inventory_page.get_inventory_text() == inventory_constants.main_nav_title

    def test_inventory_second_nav_title(self, inventory_page):
        assert inventory_page.get_products_heading_text() == inventory_constants.secondary_nav_title

    def test_copyright_text(self, inventory_page):
        assert inventory_page.get_copyright_text() == inventory_constants.copyright_text

    def test_check_empty_cart_displayed(self, inventory_page):
        assert inventory_page.get_shopping_cart_status()

    def test_sort_options_displayed(self, inventory_page):
        for sort_option in inventory_constants.sort_options:
            inventory_page.click_sort_dropdown()
            inventory_page.select_sort_dropdown_option_by_value(sort_option["Field"])
            assert inventory_page.get_sort_dropdown_text() == sort_option["Code"]
