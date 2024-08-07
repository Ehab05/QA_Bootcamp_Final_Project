import os
import unittest

from infra.UI.browser_wrapper import BrowserWrapper
from infra.json_file_handler import JsonFileHandler
from infra.utilities import Utilities
from logic.UI.contact_page import ContactPage
from logic.UI.home_page import HomePage


class TestContactPageUI(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)

    def test_send_message(self):
        """
            Test Case 016: Test Objective: Confirm that the contact message is sent successfully and appropriate
            confirmation is received.
        """

        # initialize home page and navigate to the contact page
        home_page = HomePage(self._driver)
        home_page.click_contact_button()
        contact_page = ContactPage(self._driver)

        # Perform the send contact message flow
        contact_page.insert_contact_email(Utilities().generate_random_email(self._config["email_hot"]))
        contact_page.insert_contact_name(Utilities().generate_username(8))
        contact_page.insert_contact_message(Utilities().generate_paragraph())
        contact_page.click_send_message()

        # Assert the alert message after sending
        self.assertEqual(self._config["contact_message_success"], contact_page.get_alert_text(self._driver))


