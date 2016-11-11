import os
import sys
import unittest
from log import logger
from datetime import datetime
from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = self.choose_driver('chrome')
        self.driver.maximize_window()

    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            base_path = os.path.dirname(__file__)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            dir_name = base_path + '/test_report/screenshots/'
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            self.driver.save_screenshot(dir_name + "{0}_{1}.png".format(test_method_name, now))
        self.driver.close()

    @staticmethod
    def choose_driver(driver_name):

        def firefox(): return webdriver.Firefox()

        def chrome(): return webdriver.Chrome(executable_path='chromedriver.exe')

        def opera(): return webdriver.Opera(executable_path='operadriver.exe')

        def ie(): return webdriver.Ie(executable_path="IEDriverServer.exe")

        def unknown_driver(): logger.info('Unknown driver')

        selected_driver = driver_name
        functions = {'firefox': firefox, 'chrome': chrome, 'opera': opera, 'ie': ie}
        return functions.get(selected_driver, unknown_driver)()

