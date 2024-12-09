from playwright.sync_api import Page, Locator, ConsoleMessage
from playwright.sync_api import sync_playwright


class Base:
    def __init__(self, page: Page):
        """
        Initialize basic page object
        :param page: Playwright Page
        """
        self.page = page
        self.context = page.context

        self.page.on('console', self._console_handler)

    def _console_handler(self, msg: ConsoleMessage):
        """
        Handle console message
        :param msg: console message object
        """
        if msg.type == "error":
            print(f"Console Error: {msg.text}")
        else:
            print(f"Console {msg.type}: {msg.text}")

    def open_url(self, url: str):
        """
        Open page by url
        """
        self.page.goto(url)

    def click_element(self, locator: str):
        """
        Click element by locator
        :param locator: CSS-locator
        """
        self.page.click(locator)

    def enter_text(self, locator: str, text: str):
        """
        Enter text in text field
        :param locator: CSS-locator
        :param text: text for input
        """
        self.page.fill(locator, text)

    def is_element_visible(self, locator: str, timeout: int = 5000) -> bool:
        """
        Check if element is visible
        :param locator: CSS-locator
        :param timeout: timeout in miliseconds
        :return: True, if element is visible, else False
        """
        try:
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            return True
        except:
            return False

    def get_title(self) -> str:
        """
        Return title of page
        """
        return self.page.title()

    def wait_for_load(self):
        """
        Wait for page to load
        """
        self.page.wait_for_load_state()

