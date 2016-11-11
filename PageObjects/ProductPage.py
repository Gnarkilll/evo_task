from log import log
from BasePage import BasePage
from selenium.webdriver.common.by import By
from framework.wait import is_visible, is_presence


class ProductPage(BasePage):

    """=== Locators ==="""

    popup = (By.XPATH, '//div[starts-with(@id,"popup_")]')

    @log
    def open_product(self, url='p45257130-velo-pokryshka-kenda.html'):
        self.open(url)

    @log
    def get_link_text_value(self, locator):
        return self.get_text(locator).replace('\n', ' ')

    @log
    def add_to_favorites(self, locator, wait_locator):
        self.click_and_move(locator)
        is_presence(self.driver, wait_locator)

    @log
    def remove_from_favorites(self, locator, wait_locator):
        self.move_and_click(locator)
        is_visible(self.driver, wait_locator)


class ProductInfoSection(ProductPage):

    """=== Locators ==="""

    link = (By.XPATH, '(//span[contains(@class, "b-iconed-text")]//span[@class="b-pseudo-link"])[1]')
    top_icon = (By.XPATH, '(//div[@class="b-favorites-icon__holder"]//span[contains(@class, "icon-comparison")])[1]')
    top_icon_status = (By.XPATH, '(//div[@class="b-favorites-icon__holder"]//span[contains(@class, "icon-comparison-active")])[1]')
    bottom_icon_status = (By.XPATH, '//div[@class="b-grids__item h-vertical-middle"]//span[contains(@class, "icon-comparison-active")]')

    @log
    def add_using_link(self):
        self.add_to_favorites(self.link, self.popup)

    @log
    def remove_using_link(self):
        self.remove_from_favorites(self.link, self.link)

    @log
    def add_using_icon(self):
        self.move(self.top_icon)
        is_presence(self.driver, self.popup)
        self.click(self.top_icon)
        is_presence(self.driver, self.popup)

    @log
    def remove_using_icon(self):
        self.add_to_favorites(self.top_icon, self.link)

    @log
    def get_link_text(self):
        return self.get_link_text_value(self.link)

    @log
    def is_top_icon_active(self):
        return self.active(self.top_icon_status)

    @log
    def is_bottom_icon_active(self):
        return self.active(self.bottom_icon_status)


class MovableBlock(ProductPage):

    """=== Locators ==="""

    link = (By.XPATH, '(//span[contains(@class, "b-iconed-text js-comparison-handler")]//span[@class="b-pseudo-link"])[2]')
    movable_block = (By.XPATH, '//div[@id="product_sidebar_movable"]')

    @log
    def scroll_to_movable_block(self):
        self.scroll_to_bottom()
        self.move(self.movable_block)
        is_presence(self.driver, self.movable_block)

    @log
    def add_in_movable_block(self):
        self.add_to_favorites(self.link, self.popup)

    @log
    def remove_in_movable_block(self):
        self.remove_from_favorites(self.link, self.link)

    @log
    def get_link_text(self):
        return self.get_link_text_value(self.link)


class VisitedBlock(ProductPage):

    """=== Locators ==="""

    visited_block = (By.XPATH, '//div[@class="h-clearfix"]')
    icon = (By.XPATH, '(//div[@class="b-slider__frame"]//span[contains(@class, "h-vertical-middle")])[1]')
    product_img = (By.XPATH, '(//div[@class="b-slider__frame"]//img[@class="b-image-holder__img"])[1]')
    icon_status = (By.XPATH, '(//div[@class="b-favorites-icon__holder"]//span[contains(@class, "icon-comparison-active")])[2]')

    @log
    def scroll_to_visited_block(self):
        self.scroll_to_bottom()
        self.move(self.visited_block)
        is_presence(self.driver, self.visited_block)
        is_presence(self.driver, self.product_img)

    @log
    def add_in_visited_block(self):
        self.move(self.product_img)
        is_presence(self.driver, self.icon)
        self.move(self.icon)
        is_presence(self.driver, self.popup)
        self.click(self.icon)
        is_presence(self.driver, self.popup)

    @log
    def remove_in_visited_block(self):
        self.move(self.icon)
        is_presence(self.driver, self.popup)
        self.click(self.icon)

    @log
    def is_icon_active(self):
        return self.active(self.icon_status)
