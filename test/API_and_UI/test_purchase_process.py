import os
import unittest
from infra.API.api_wrapper import APIWrapper
from infra.UI.browser_wrapper import BrowserWrapper
from infra.json_file_handler import JsonFileHandler
from infra.utilities import Utilities
from logic.API.API_login_page import APILoginPage
from logic.UI.cart_page import CartPage
from logic.UI.home_page import HomePage
from logic.UI.place_order_page import PlaceOrderPage
from logic.UI.product_page import ProductPage
from logic.UI.success_purchase_page import SuccessPurchasePage
from logic.utilities_logic import UtilitiesLogic


class TestPurchaseProcess(unittest.TestCase):
    def setUp(self):
        self._request = APIWrapper()
        self._driver = BrowserWrapper().get_driver()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)

    def test_purchase_2_products_with_registered_user(self):
        # Pre-conditions
        credit_card = UtilitiesLogic().generate_random_credit_card(self._config["credit_card_type"])
        login_api = APILoginPage(self._request)
        token = login_api.login_flow_through_api()
        home_page = HomePage(self._driver)
        home_page.add_token_to_cookie(token)
        # Add first product from the first section of home page
        home_page.click_on_product_by_name(home_page.get_random_product_title())
        product_page = ProductPage(self._driver)
        product_page.click_add_to_cart_button()
        product_page.accept_alert()
        # Add second product from the second section of home page
        product_page.click_product_store_button()
        home_page = HomePage(self._driver)
        home_page.click_next_button()
        home_page.click_on_product_by_name(home_page.get_random_product_title())
        product_page = ProductPage(self._driver)
        product_page.click_add_to_cart_button()
        product_page.accept_alert()
        # Navigate to the cart page and click place order button
        product_page.click_cart_button()
        cart_page = CartPage(self._driver)
        cart_page.click_place_order_button()
        place_order_page = PlaceOrderPage(self._driver)
        # Perform the purchase flow
        place_order_page.insert_name_input(Utilities().generate_username(5))
        place_order_page.insert_country_input(Utilities().generate_username(6))
        place_order_page.insert_city_input(Utilities().generate_username(7))
        place_order_page.insert_card_number_input(["card_number"])
        place_order_page.insert_month_input(credit_card["card_expiry"].split('/')[0])
        place_order_page.insert_year_input(credit_card["card_expiry"].split('/')[1])
        place_order_page.click_purchase_button()
        success_purchase_page = SuccessPurchasePage(self._driver)

        # Assert the purchase success message
        self.assertEqual(self._config["purchase_success_message"], success_purchase_page.get_purchase_success_message())
