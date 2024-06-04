import pytest
import allure
from playwright.sync_api import sync_playwright
from pathlib import Path


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
def page(request, browser):
    context = browser.new_context\
            (
                record_video_dir='report/',
                record_video_size={'width': 1280, 'height': 720}
            )
    page = context.new_page()
    yield page
    context.close()

    # Check if the test failed and the video was recorded
    if request.node.rep_call.failed:
        # Retrieve the video path from the page
        video_path = page.video.path() if page.video else None
        if video_path:
            video_path = Path(video_path)
            allure.attach.file(video_path, name="Video evidence", attachment_type=allure.attachment_type.WEBM)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This ensures that the report hooks can access the outcome of each test
    outcome = yield
    report = outcome.get_result()

    # Attach the report to the test item for access in fixtures
    setattr(item, "rep_" + report.when, report)
