from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver, base_url='http://www.prom.ua/'):
        self.driver = driver
        self.base_url = base_url

    def open(self, page_url, view_mode=None):
        url = self.base_url + page_url
        if view_mode:
            url = url + '?output={}'.format(view_mode)
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def move(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def move_and_click(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def click_and_move(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).click(element).move_to_element(element).perform()

    def click_and_hold(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).click_and_hold(element).perform()

    def clear(self, locator):
        self.driver.find_element(*locator).clear()

    def set_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def exist(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def active(self, locator):
        return True if self.exist(locator) else False

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

