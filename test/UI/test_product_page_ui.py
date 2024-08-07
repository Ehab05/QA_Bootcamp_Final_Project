import os
import unittest

from infra.UI.browser_wrapper import BrowserWrapper
from infra.json_file_handler import JsonFileHandler
from logic.UI.home_page import HomePage
from logic.UI.product_page import ProductPage


class TestProductPageUI(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)

    def tearDown(self):
        self._driver.quit()

    def test_add_to_cart_with_unregistered_user(self):
        """
            Test Case 019: Verify Success Message Displayed Upon Clicking "Add to Cart" Button.
        """
        # Initialize Home Page
        home_page = HomePage(self._driver)

        # Click on the product by its name and add to cart
        home_page.click_on_product_by_name(self._config["add_product_by_name"])
        product_page = ProductPage(self._driver)
        product_page.click_add_to_cart_button()

        # Assert success message
        self.assertEqual(self._config["add_to_cart_success_message"], product_page.get_alert_text(self._driver))
