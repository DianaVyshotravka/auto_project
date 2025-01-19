import pytest
from playwright.sync_api import sync_playwright


class BaseTest:
    BASE_URL = "https://ultimateqa.com/automation"
    DEFAULT_BROWSER = "chromium"
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, request: pytest.FixtureRequest):
        """
        Fixture for setting up and tearing down Playwright resources.

        Parameters
        ----------
        request : The request object which allows access to test-specific parameters,
        including the browser type specified when running the test.
        """
        browser_type = getattr(request, "param", self.DEFAULT_BROWSER)
        self.playwright = sync_playwright().start()

        if browser_type == "chromium":
            self.browser = self.playwright.chromium.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        yield

        self.browser.close()
        self.playwright.stop()
