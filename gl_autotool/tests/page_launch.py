from gl_autotool.pages.basic_page import Base
from gl_autotool.tests.base_test import BaseTest


class LaunchTest(BaseTest):
    def test_page_load(self):
        """
        Test to verify if web page is loaded and if yes, gets its title
        """
        self.set_up()

        try:
            base_page = Base(self.page)
            url = "https://ultimateqa.com/automation"
            base_page.open_url(url)
            base_page.wait_for_load()
            title = base_page.get_title()
            print(f"Page title: {title}")

            assert title == "Automation Practice - Ultimate QA", \
                "Wrong title"
        finally:
            self.tear_down()


# if __name__ == "__main__":
#     test = LaunchTest()
#     test.test_page_load()
