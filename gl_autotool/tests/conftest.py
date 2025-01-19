import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(autouse=True)
def setup_and_teardown(request: pytest.FixtureRequest):
    """
    Fixture for setting up and tearing down Playwright resources.

    Parameters
    ----------
    request: The request object which allows access to test-specific parameters,
    including the browser type specified when running the test.
    """
    default_browser = "chromium"
    browser_type = getattr(request, "param", default_browser)
    playwright = sync_playwright().start()

    if browser_type == "chromium":
        browser = playwright.chromium.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")

    context = browser.new_context()
    page = context.new_page()

    yield page

    browser.close()
    playwright.stop()
