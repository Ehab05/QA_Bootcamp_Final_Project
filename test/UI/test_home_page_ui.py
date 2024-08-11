import os
import unittest
from infra.UI.browser_wrapper import BrowserWrapper
from infra.json_file_handler import JsonFileHandler
from logic.UI.home_page import HomePage
from logic.UI.login_page import LoginPage


class TestHomePageUI(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        self._config = JsonFileHandler().load_from_file('../../demo_blaze_config.json', __file__)

    def tearDown(self):
        self._driver.quit()

    def test_home_page_logout(self):
        """
             Test Case 014: Verify successful logout
        """
        # Initialize home page
        home_page = HomePage(self._driver)

        # Pre-conditions
        home_page.click_login_button()
        login_page = LoginPage(self._driver)
        login_page.insert_username(self._config["username"])
        login_page.insert_password(self._config["password"])
        login_page.click_login_button()
        home_page = HomePage(self._driver)

        # Performing the logout
        home_page.click_logout_button()
        home_page = HomePage(self._driver)

        # Assert Login button and sign up appears in the menu
        self.assertEqual(home_page.get_login_button_text(), "Log in")
        self.assertEqual(home_page.get_sign_up_button_text(), "Sign up")
