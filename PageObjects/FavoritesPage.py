from log import log, logger
from random import choice
from BasePage import BasePage
from framework.wait import is_visible
from string import ascii_letters, digits
from selenium.webdriver.common.by import By


class FavoritesPage(BasePage):

    """=== Locators ==="""

    title = (By.CSS_SELECTOR, '.h-layout-left.big-text')
    all_products_tab = (By.XPATH, '//li[contains(@class, "tab_state_active")]/a[@class="b-tabs__link"]')
    category_tab = (By.XPATH, '//li[normalize-space(@class)="b-tabs__tab"]/a')
    tab_title = (By.XPATH, '//li[contains(@class, "tab_state_active")]/a')
    close_icon = (By.XPATH, '(//div[@class="b-products-compare__part"]/div/span)[1]')
    send_to_mail_btn = (By.ID, 'comparison_send_to_email')
    send_btn = (By.ID, 'submit_button')
    email_field = (By.ID, 'comparison-email')
    successfully_message = (By.CSS_SELECTOR, '.b-info-panel__wrap-text')

    @log
    def open_favorites(self):
        self.open('comparison/list')

    @log
    def get_title(self):
        return self.get_text(self.title)

    @log
    def parse(self):
        return self.get_text(self.tab_title)

    @log
    def get_category_tab_title(self):
        return ' '.join([i for i in self.parse().split(' ') if i.isalpha()])

    @log
    def get_category_tab_counter(self):
        return int(''.join([i for i in self.parse().split(' ') if i.isdigit()]))

    def get_all_products_tab_title(self):
        pass

    def get_all_products_tab_counter(self):
        pass

    @log
    def get_message(self):
        return self.get_text(self.successfully_message)

    @log
    def select_category_tab(self):
        self.click(self.category_tab)

    @log
    def select_all_products_tab(self):
        self.click(self.all_products_tab)

    @log
    def remove_from_favorites(self):
        self.click(self.close_icon)

    @log
    def open_send_mail_window(self):
        self.click(self.send_to_mail_btn)
        is_visible(self.driver, self.send_btn)

    @log
    def fill_email(self, email_length):
        generate_sequence = ''.join(choice(ascii_letters + digits) for _ in range(email_length))
        email = generate_sequence + '@sharklasers.com'
        self.set_text(self.email_field, email)
        logger.info('Mail was sent to {}'.format(email))

    @log
    def send_mail(self):
        self.click(self.send_btn)
        is_visible(self.driver, self.successfully_message)




