from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException


def wait_conditions(wait_condition, locator):

    presence_of_element_located = lambda: ec.presence_of_element_located(locator)
    visibility_of_element_located = lambda: ec.visibility_of_element_located(locator)
    unknown_waiter = lambda: 'Unknown waiter'

    condition = wait_condition
    functions = {'presence_of_element_located': presence_of_element_located,
                 'visibility_of_element_located': visibility_of_element_located}
    return functions.get(condition, unknown_waiter)()


def wait_for(driver, locator, wait_condition):
    try:
        WebDriverWait(driver, 10).until(wait_conditions(wait_condition, locator))
    except (ElementNotVisibleException, NoSuchElementException):
        pass


def is_presence(driver, locator):
    wait_for(driver, locator, 'presence_of_element_located')


def is_visible(driver, locator):
    wait_for(driver, locator, 'visibility_of_element_located')


