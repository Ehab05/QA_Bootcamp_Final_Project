import unittest
from infra.UI.browser_wrapper import BrowserWrapper
from infra.utilities import Utilities
from logic.UI.home_page import HomePage
from logic.UI.sign_up_page import SignUpPage


class TestSignUpPageUI(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()

    def tearDown(self):
        self._driver.quit()

    def test_valid_sign_up(self):
        """
            Test Case 003: Verify successful sign up with valid username and password
        """

        # Initialize home page
        home_page = HomePage(self._driver)

        # perform signup flow
        home_page.click_sign_up_button()
        sign_up_page = SignUpPage(self._driver)
        sign_up_page.insert_username(Utilities().generate_username(8))
        sign_up_page.insert_password(Utilities().generate_random_password(8))
        sign_up_page.click_sign_up_button()

        # assert the signup result
        self.assertEqual(sign_up_page.get_success_signup_message(), sign_up_page.get_alert_text(self._driver))

    def test_sign_up_with_username_only(self):
        """
            Test Case 004: Verify that a user receives an appropriate error message when attempting to sign in with a
            valid username but without providing a password.
        """
        # Initialize home page
        home_page = HomePage(self._driver)

        # perform signup flow
        home_page.click_sign_up_button()
        sign_up_page = SignUpPage(self._driver)
        sign_up_page.insert_username(Utilities().generate_username(8))
        sign_up_page.clear_password_input_field()
        sign_up_page.click_sign_up_button()

        # assert the signup result
        self.assertEqual(sign_up_page.get_signup_missing_fields_message(), sign_up_page.get_alert_text(self._driver))

    def test_sign_up_with_password_only(self):
        """
             Test Case 005:  Verify that a user receives an appropriate error message when attempting to sign in with
             a valid password but without providing a username.
        """
        # Initialize home page
        home_page = HomePage(self._driver)

        # perform signup flow
        home_page.click_sign_up_button()
        sign_up_page = SignUpPage(self._driver)
        sign_up_page.clear_username_input_field()
        sign_up_page.insert_password(Utilities().generate_random_password(8))
        sign_up_page.click_sign_up_button()

        # assert the signup result
        self.assertEqual(sign_up_page.get_signup_missing_fields_message(), sign_up_page.get_alert_text(self._driver))

