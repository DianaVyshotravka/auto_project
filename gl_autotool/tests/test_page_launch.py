from gl_autotool.pages.base_page import BasePage
from gl_autotool.tests.base_test import BaseTest


class TestLaunchPage(BaseTest):
    """
    Test class for verifying web page loading and title.
    """

    def test_page_load(self):
        """
        Test to verify if web page is loaded and gets its title.
        """
        url = self.BASE_URL
        page = BasePage(self.page)
        page.open_url(url)
        title = page.get_title()

        assert title == "Automation Practice - Ultimate QA", f"Wrong title: {title}"
