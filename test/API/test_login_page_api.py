import os
import unittest
from infra.API.api_wrapper import APIWrapper
from infra.json_file_handler import JsonFileHandler
from infra.utilities import Utilities
from logic.API.API_login_page import APILoginPage
from logic.utilities_logic import UtilitiesLogic


class TestLoginPageAPI(unittest.TestCase):
    def setUp(self):
        self._request = APIWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)

    def tearDown(self):
        pass

    def test_valid_login(self):
        """
            Test Case 006:  Verify successful login with valid user name and password
        """

        # Initialize API page
        login_api = APILoginPage(self._request)
        username, password = login_api.get_username_and_password()

        # Send the API call
        response = login_api.login_via_api(username, password)

        # Assert the response
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.ok)
        self.assertIsNotNone(login_api.check_auth_token(response.text)["Auth_token"])

    def test_login_with_invalid_password(self):
        """
             Test Case 007:   Ensure the display of the correct error message when attempting to log in with a
             valid username and an incorrect password.
        """

        # Initialize API page and arrange the username and password
        login_api = APILoginPage(self._request)
        username = self._config.get("username")
        password = self._config.get("password")

        # Send the API call
        response = login_api.login_via_api(username, password)

        # Assert the response
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.ok)
        self.assertTrue(self._config["login_password_error_message"] == login_api.get_response_json(response)["errorMessage"])

    def test_login_with_no_registered_user(self):
        """
            Test Case 008:  Ensure the display of the correct error message when attempting to log in with an
            unregistered username and any password.
        """

        # Initialize API page and arrange the username and password
        login_api = APILoginPage(self._request)
        username = Utilities().generate_username(15)
        password = self._config.get("password")

        # Send the API call
        response = login_api.login_via_api(username, password)

        # Assert the response
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.ok)
        self.assertEqual(self._config["login_user_error_message"], UtilitiesLogic().get_response_json(response)["errorMessage"])


