from playwright.sync_api import Page, Locator, ConsoleMessage
from playwright.sync_api import sync_playwright


class Base:
    def __init__(self, page: Page):
        """
        Ініціалізує базовий об'єкт сторінки.
        :param page: Об'єкт Playwright Page
        """
        self.page = page
        self.context = page.context

        self.page.on('console', self._console_handler)

    def _console_handler(self, msg: ConsoleMessage):
        """
        Обробляє повідомлення з консолі браузера.
        :param msg: Об'єкт повідомлення з консолі
        """
        if msg.type == "error":
            print(f"Console Error: {msg.text}")
        else:
            print(f"Console {msg.type}: {msg.text}")

    def open_url(self, url: str):
        """
        Відкриває сторінку за вказаним URL.
        """
        self.page.goto(url)

    def click_element(self, locator: str):
        """
        Натискає на елемент за селектором.
        :param locator: CSS-селектор
        """
        self.page.click(locator)

    def enter_text(self, locator: str, text: str):
        """
        Вводить текст у поле.
        :param locator: CSS-селектор
        :param text: Текст для введення
        """
        self.page.fill(locator, text)

    def is_element_visible(self, locator: str, timeout: int = 5000) -> bool:
        """
        Перевіряє, чи видимий елемент.
        :param locator: CSS-селектор
        :param timeout: Тайм-аут в мілісекундах
        :return: True, якщо елемент видимий
        """
        try:
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            return True
        except:
            return False

    def get_title(self) -> str:
        """
        Повертає заголовок сторінки.
        """
        return self.page.title()

    def wait_for_load(self):
        """
        Очікує завершення завантаження сторінки.
        """
        self.page.wait_for_load_state()

