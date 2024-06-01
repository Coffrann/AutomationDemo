import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run playwright tests in headless mode"
    )


@pytest.fixture(scope="session")
def browser(pytestconfig):
    headless_arg = pytestconfig.getoption("--headless")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless_arg)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
