from playwright.sync_api import Page, ConsoleMessage
from structlog import get_logger


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)
        self.context = page.context
        self.page.on('console', self._console_handler)

    def _console_handler(self, msg: ConsoleMessage) -> None:
        """
        Handle console messages and log them.
        This method is triggered whenever a console message is logged
        on the web page being tested.

        Parameters
        ----------
        msg : ConsoleMessage
        The console message object emitted by the web page.
        """
        if msg.type == "error":
            self.logger.error(f"Console Error: {msg.text}")
        else:
            self.logger.info(f"Console {msg.type}: {msg.text}")

    def open_url(self, url: str, timeout: int = 30000) -> None:
        """
        Open page by URL and wait for it to load.

        Parameters
        ----------
        url : str
            The URL to navigate to.
        timeout : int
            Maximum time to wait for navigation in milliseconds (default: 30s).
        """
        self.logger.info(f"Opening URL: {url}")
        self.page.goto(url, timeout=timeout)
        self.page.wait_for_load_state()

    def get_title(self) -> str:
        """
        Return the page title.

        Returns
        -------
        str
            The title of the page.
        """
        title = self.page.title()
        self.logger.info(f"Page title retrieved: {title}")
        return title
