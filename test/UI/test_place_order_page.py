import os
import unittest
from infra.UI.browser_wrapper import BrowserWrapper
from infra.json_file_handler import JsonFileHandler
from infra.utilities import Utilities
from logic.UI.cart_page import CartPage
from logic.UI.home_page import HomePage
from logic.UI.login_page import LoginPage
from logic.UI.place_order_page import PlaceOrderPage
from logic.UI.product_page import ProductPage
from logic.UI.success_purchase_page import SuccessPurchasePage


class TestPlaceOrderPageUI(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)

    def tearDown(self):
        self._driver.quit()

    def test_purchase_product_by_name_with_unregistered_user(self):
        """
             Test Case 020:  Verify Success Message Displayed Upon Purchasing a Product by Name with a Unregistered User.
        """

        # Pre-conditions
        credit_card = Utilities().generate_random_credit_card(self._config["credit_card_type"])
        home_page = HomePage(self._driver)

        # Navigate to the product page and perform the purchase process
        home_page.click_on_product_by_name(self._config["purchase_product"])
        product_page = ProductPage(self._driver)
        product_page.click_add_to_cart_button()
        product_page.accept_alert()
        product_page.click_cart_button()
        cart_page = CartPage(self._driver)
        cart_page.click_place_order_button()
        place_order_page = PlaceOrderPage(self._driver)
        place_order_page.insert_name_input(Utilities().generate_username(5))
        place_order_page.insert_country_input(Utilities().generate_username(6))
        place_order_page.insert_city_input(Utilities().generate_username(7))
        place_order_page.insert_card_number_input(["card_number"])
        place_order_page.insert_month_input(credit_card["card_expiry"].split('/')[0])
        place_order_page.insert_year_input(credit_card["card_expiry"].split('/')[1])
        place_order_page.click_purchase_button()
        success_purchase_page = SuccessPurchasePage(self._driver)

        # Assert successful purchase message
        self.assertEqual(self._config["purchase_success_message"], success_purchase_page.get_purchase_success_message())

    def test_purchase_product_by_name_with_registered_user(self):
        """
             Test Case 021:   Verify Success Message Displayed Upon Purchasing a Product by Name with a Registered User.
        """

        # Pre-conditions
        credit_card = Utilities().generate_random_credit_card(self._config["credit_card_type"])
        home_page = HomePage(self._driver)
        home_page.click_login_button()
        login_page = LoginPage(self._driver)
        login_page.login_flow()
        home_page = HomePage(self._driver)

        # Navigate to the product page and perform the purchase process
        home_page.click_on_product_by_name(self._config["purchase_product"])
        product_page = ProductPage(self._driver)
        product_page.click_add_to_cart_button()
        product_page.accept_alert()
        product_page.click_cart_button()
        cart_page = CartPage(self._driver)
        cart_page.click_place_order_button()
        place_order_page = PlaceOrderPage(self._driver)
        place_order_page.insert_name_input(Utilities().generate_username(5))
        place_order_page.insert_country_input(Utilities().generate_username(6))
        place_order_page.insert_city_input(Utilities().generate_username(7))
        place_order_page.insert_card_number_input(["card_number"])
        place_order_page.insert_month_input(credit_card["card_expiry"].split('/')[0])
        place_order_page.insert_year_input(credit_card["card_expiry"].split('/')[1])
        place_order_page.click_purchase_button()
        success_purchase_page = SuccessPurchasePage(self._driver)

        # Assert successful purchase message
        self.assertEqual(self._config["purchase_success_message"], success_purchase_page.get_purchase_success_message())
