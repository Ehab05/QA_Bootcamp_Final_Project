import unittest
from infra.UI.browser_wrapper import BrowserWrapper


class TestBasePage(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()

    def tearDown(self):
        self._driver.quit()

    def test_base_page(self):
        pass
