#!/usr/bin/python
# -*- coding: utf-8 -*-

from log import log
from BasePage import BasePage
from selenium.webdriver.common.by import By
from framework.wait import is_visible, is_presence


class AllProductsPage(BasePage):

    """=== Locators ==="""

    a_favorites_link = (By.XPATH, '(//span[contains(text(), "Добавить в избранное")])[1]')
    r_favorites_link = (By.XPATH, '(//span[contains(text(), "Убрать из избранного")])[1]')
    popup = (By.XPATH, '//div[starts-with(@id, "popup_")]')
    top_icon = (By.XPATH, '(//div[@class="b-favorites-icon__holder"]//span[contains(@class, "icon-comparison")])[1]')
    top_icon_status = (By.XPATH, '(//div[@class="b-favorites-icon__holder"]//span[contains(@class, "icon-comparison-active")])[1]')
    item_block = (By.XPATH, '(//div[@class="b-product-list__column"])[1]')
    redirect_button = (By.XPATH, '//div[starts-with(@id, "popup_")]//a[contains(@class, "b-button")]')
    favorites_page_title = (By.CSS_SELECTOR, '.h-layout-left.big-text')

    @log
    def do_mouse_over_on_product(self, locator):
        self.move(locator)
        is_visible(self.driver, self.a_favorites_link)

    @log
    def add_using_link(self):
        self.click_and_move(self.a_favorites_link)
        is_presence(self.driver, self.popup)

    @log
    def remove_using_link(self):
        self.move_and_click(self.r_favorites_link)
        is_visible(self.driver, self.a_favorites_link)

    @log
    def add_from_icon(self, locator, wait_locator):
        self.move(locator)
        is_presence(self.driver, wait_locator)
        self.click(locator)
        is_presence(self.driver, wait_locator)

    @log
    def remove_using_icon(self):
        self.click(self.top_icon)
        is_visible(self.driver, self.a_favorites_link)

    @log
    def is_top_icon_active(self):
        return self.active(self.top_icon_status)

    @log
    def is_bottom_icon_active(self, locator):
        return self.active(locator)

    @log
    def get_link_text_value(self, locator):
        return self.get_text(locator)


class GalleryMode(AllProductsPage):

    """=== Locators ==="""

    product = (By.XPATH, '(//div[@class="b-product-gallery__content"])[1]')
    link_text = (By.XPATH, '(//div[@class="h-mt-5"]//span[@class="b-pseudo-link"]/span)[1]')
    icon_status = (By.XPATH, '(//div[@class="h-mt-5"]//span[contains(@class, "icon-comparison-active")])[1]')

    @log
    def gallery_mode(self):
        self.open('Velosipednye-shiny', 'gallery')

    @log
    def select_product(self):
        self.do_mouse_over_on_product(self.product)

    @log
    def add_using_icon(self):
        self.add_from_icon(self.top_icon, self.popup)

    @log
    def get_icon_status(self):
        return self.is_bottom_icon_active(self.icon_status)

    @log
    def get_link_text(self):
        return self.get_link_text_value(self.link_text)

    @log
    def redirect_using_link(self):
        self.add_using_link()
        self.move_and_click(self.redirect_button)
        is_presence(self.driver, self.favorites_page_title)

    @log
    def redirect_using_icon(self):
        self.add_using_icon()
        self.move_and_click(self.redirect_button)
        is_presence(self.driver, self.favorites_page_title)


class ListMode(AllProductsPage):

    """=== Locators ==="""

    product = (By.XPATH, '(//div[@class="b-product-line"]/div)[2]')
    link_text = (By.XPATH, '(//div[@class="b-product-list__compare"]//span[@class="b-pseudo-link"]/span)[1]')
    icon_status = (By.XPATH, '(//div[@class="b-product-list__compare"]//span[contains(@class, "icon-comparison-active")])[1]')

    @log
    def list_mode(self):
        self.open('Velosipednye-shiny', 'list')

    @log
    def select_product(self):
        self.do_mouse_over_on_product(self.product)

    @log
    def add_using_icon(self):
        self.move(self.item_block)
        self.add_from_icon(self.top_icon, self.popup)

    @log
    def get_icon_status(self):
        return self.is_bottom_icon_active(self.icon_status)

    @log
    def get_link_text(self):
        return self.get_link_text_value(self.link_text)
