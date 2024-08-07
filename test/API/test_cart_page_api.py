import os
import unittest

from infra.API.api_wrapper import APIWrapper
from infra.UI.browser_wrapper import BrowserWrapper
from infra.json_file_handler import JsonFileHandler
from logic.API.API_cart_page import APICartPage
from logic.API.API_login_page import APILoginPage
from logic.utilities_logic import UtilitiesLogic


class TestCartPageAPI(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        self._request = APIWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)

    def tearDown(self):
        self._driver.quit()

    def test_view_cart_with_unregistered_user(self):
        """
            Test Case 017:  Validate that the cart items are correctly retrieved via the API with unregistered user
        """
        # Initialize API page

        view_cart_api = APICartPage(self._request)

        # Send the API request(post request with the endpoint and user cookie)
        response = view_cart_api.view_cart_with_unregistered_user_via_api(self._driver)
        cart_items = UtilitiesLogic().get_response_json(response).get("Items")

        # Assert the response
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.ok)
        self.assertEqual(cart_items, self._config["unregistered_user_cart_list"])

    def test_view_cart_with_registered_user(self):
        """
            Test Case 018:  Validate that the cart items are correctly retrieved via the API With Registered User.
        """
        # Pre-conditions Initialize API login page and extract token
        login_api = APILoginPage(self._request)
        username, password = login_api.get_username_and_password()
        response = login_api.login_via_api(username, password)
        auth_token = login_api.extract_auth_token(response.text)

        # Initialize API cart page
        view_cart_api = APICartPage(self._request)

        # Send the API request: post request with the endpoint and user cookie(auth token)
        response = view_cart_api.view_cart_with_registered_user_via_api(auth_token)
        cart_list = UtilitiesLogic().get_response_json(response)

        # Assert the response
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.ok)
        self.assertIsInstance(cart_list, dict)
        self.assertIsInstance(cart_list["Items"], list)
