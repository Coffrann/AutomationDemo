class BasePage:
    def __init__(self, page):
        """
        Initializes the page instance with the Playwright 'page' object.

        :param page: The Playwright 'page' object representing a browser tab.
        """
        self.page = page

    def get_current_url(self):
        """
        Gets the current URL.

        :return: The URL of the current page as a string.
        """
        return self.page.url

    def navigate(self, url: str):
        """
        Navigates to the specified URL.

        :param url: The URL to navigate to.
        """
        self.page.goto(url)

    def get_title(self):
        """
        Gets the title of the current page.

        :return: The title of the page as a string.
        """
        return self.page.title()

    def fill_text_field(self, selector: str, text: str):
        """
        Fills a text field identified by the selector with the provided text.

        :param selector: The selector of the text field.
        :param text: The text to be entered into the field.
        """
        self.page.fill(selector, text)

    def click_element(self, selector: str):
        """
        Clicks an element identified by the selector.

        :param selector: The selector of the element to be clicked.
        """
        self.page.click(selector)

    def get_text(self, selector: str):
        """
        Gets the text content of an element identified by the selector.

        :param selector: The selector of the element from which to get the text.
        :return: The text content of the element as a string.
        """
        return self.page.text_content(selector)

    def is_element_visible(self, selector: str):
        """
        Checks if an element identified by the selector is visible on the page.

        :param selector: The selector of the element to check.
        :return: True if the element is visible, False otherwise.
        """
        return self.page.is_visible(selector)

    def select_option_by_value(self, selector: str, value: str):
        """
        Selects an option from a dropdown (select element) by its value.

        :param selector: The selector of the select element.
        :param value: The value of the option to be selected.
        """
        self.page.select_option(selector, value)

    def select_option_by_label(self, selector: str, label: str):
        """
        Selects an option from a dropdown (select element) by its label.

        :param selector: The selector of the select element.
        :param label: The label of the option to be selected.
        """
        self.page.select_option(selector, label=label)

    def select_option_by_index(self, selector: str, index: int):
        """
        Selects an option from a dropdown (select element) by its index.

        :param selector: The selector of the select element.
        :param index: The index of the option to be selected.
        """
        self.page.select_option(selector, index=index)

    def get_selected_option(self, selector: str):
        """
        Gets the selected option from a <select> element.

        :param selector: The selector of the <select> element.
        :return: The value of the selected option.
        """
        selected_option = self.page.eval_on_selector(selector, "element => element.value")
        return selected_option

    @classmethod
    def data_test(cls, data_test_value: str):
        """
        Selects an element by its data-test attribute value.

        :param data_test_value: The value of the data-test attribute.
        :return: The locator for the element with the specified data-test value.
        """
        return f'[data-test="{data_test_value}"]'
