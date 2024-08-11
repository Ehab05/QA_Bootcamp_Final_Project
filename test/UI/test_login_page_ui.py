import os
import unittest
from infra.UI.browser_wrapper import BrowserWrapper
from infra.json_file_handler import JsonFileHandler
from infra.utilities import Utilities
from logic.UI.home_page import HomePage
from logic.UI.login_page import LoginPage


class TestLoginPageUI(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        self._config = JsonFileHandler().load_from_file('../../demo_blaze_config.json', __file__)

    def tearDown(self):
        self._driver.quit()

    def test_valid_log_in(self):
        """
             Test Case 009:  Verify successful login with valid username and password via UI
        """
        # Initialize home page
        home_page = HomePage(self._driver)

        # Performing login flow
        home_page.click_login_button()
        login_page = LoginPage(self._driver)
        login_page.insert_username(self._config["username"])
        login_page.insert_password(self._config["password"])
        login_page.click_login_button()
        home_page = HomePage(self._driver)

        # Asserting the welcome message
        self.assertEqual(home_page.get_login_success_message(), home_page.get_name_of_user())

    def test_log_in_with_username_only(self):
        """
             Test Case 010:  Verify that a user receives an appropriate error message when attempting to log in with a
             valid username but without providing a password.
        """
        # Initialize home page
        home_page = HomePage(self._driver)

        # Performing login flow
        home_page.click_login_button()
        login_page = LoginPage(self._driver)
        login_page.insert_username(self._config["username"])
        login_page.clear_password_input_field()
        login_page.click_login_button()

        # Asserting the welcome message
        self.assertEqual(login_page.get_alert_text(self._driver), login_page.get_login_missing_fields_message())

    def test_log_in_with_password_only(self):
        """
             Test Case 011:  Verify that a user receives an appropriate error message when attempting to log in with a
             valid password but without providing a username.
        """
        # Initialize home page
        home_page = HomePage(self._driver)

        # Performing login flow
        home_page.click_login_button()
        login_page = LoginPage(self._driver)
        login_page.clear_username_input_field()
        login_page.insert_password(self._config["password"])
        login_page.click_login_button()

        # Asserting the welcome message
        self.assertEqual(login_page.get_alert_text(self._driver), login_page.get_login_missing_fields_message())

    def test_log_in_with_invalid_password(self):
        """
             Test Case 012:  Verify that a user receives an appropriate error message when attempting to log in with a
             valid username and invalid password.
        """
        # Initialize home page
        home_page = HomePage(self._driver)

        # Performing login flow
        home_page.click_login_button()
        login_page = LoginPage(self._driver)
        login_page.insert_username(self._config["username"])
        login_page.insert_password(Utilities().scramble_password(self._config["password"]))
        login_page.click_login_button()

        # Asserting the welcome message
        self.assertEqual(login_page.get_alert_text(self._driver), login_page.get_invalid_password_message())

