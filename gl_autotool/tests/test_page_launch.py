from gl_autotool.pages.base_page import BasePage
from gl_autotool.tests.base_test import BaseTest


class TestLaunchPage(BaseTest):
    """
    Test class for verifying web page loading and title.
    """

    def test_page_load(self, setup_and_teardown):
        """
        Test to verify if web page is loaded and gets its title.
        """
        page = BasePage(setup_and_teardown)
        page.open_url(self.base_url)
        title = page.get_title()

        assert title == "Automation Practice - Ultimate QA", f"Wrong title: {title}"
