from gl_autotool.pages.basic_page import Base
from gl_autotool.tests.base_test import BaseTest


class TestLaunchPage(BaseTest):
    """
    Test class for verifying web page loading and title.
    """

    def test_page_load(self):
        """
        Test to verify if web page is loaded and gets its title.
        """
        base_page = Base(self.page)
        url = "https://ultimateqa.com/automation"
        base_page.open_url(url)
        base_page.wait_for_load()
        title = base_page.get_title()

        print(f"Page title: {title}")
        assert title == "Automation Practice - Ultimate QA", "Wrong title"
