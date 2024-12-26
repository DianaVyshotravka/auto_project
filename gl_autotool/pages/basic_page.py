from playwright.sync_api import Page, ConsoleMessage


class Base:
    def __init__(self, page: Page):
        self.page = page
        self.context = page.context

        self.page.on('console', self._console_handler)

    def _console_handler(self, msg: ConsoleMessage) -> None:
        """
        Handle console message

        Parameters
        ----------
        msg
        """
        if msg.type == "error":
            print(f"Console Error: {msg.text}")
        else:
            print(f"Console {msg.type}: {msg.text}")
        return

    def open_url(self, url: str) -> None:
        """
        Open page by url

        Parameters
        ----------
        url
        """
        self.page.goto(url)
        return

    def get_title(self) -> str:
        """
        Return title of page
        """
        return self.page.title()

    def wait_for_load(self) -> None:
        """
        Wait for page to load
        """
        self.page.wait_for_load_state()
        return
