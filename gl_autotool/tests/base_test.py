import pytest
from playwright.sync_api import sync_playwright

DEFAULT_BROWSER = "chromium"

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, request):
        """
        Fixture for setting up and tearing down Playwright resources.
        """
        browser_type = getattr(request, "param", DEFAULT_BROWSER)
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
