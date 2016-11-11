from log import log
from BasePage import BasePage
from framework.wait import is_visible
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class HeaderContentMenu(BasePage):

    """=== Locators ==="""

    favorites_counter = (By.XPATH, '//span[@id="favorite_products"]//span[contains(@class, "link-counter")]')
    favorites_page_title = (By.CSS_SELECTOR, '.h-layout-left.big-text')

    @log
    def get_amount_of_favorites_items(self):
        try:
            return int(self.get_text(self.favorites_counter))
        except NoSuchElementException:
            return 0

    @log
    def open_favorites_page(self):
        self.click(self.favorites_counter)
        is_visible(self.driver, self.favorites_page_title)
