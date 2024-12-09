import pytest
from playwright.sync_api import sync_playwright


class BaseTest:

    def set_up(self, browser_type="chromium"):
        """Preconditions and setup before test execution"""
        self.playwright = sync_playwright().start()
        if browser_type == "chromium":
            self.browser = self.playwright.chromium.launch(headless=False)
        # elif browser_type == 'firefox':
        #     self.browser = self.playwright.firefox.launch(headless=False)
        # elif browser_type == 'webkit':
        #     self.browser = self.playwright.webkit.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def tear_down(self):
        """Postconditions"""
        self.browser.close()
        self.playwright.stop()