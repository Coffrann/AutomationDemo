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
