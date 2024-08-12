
import unittest
from infra.UI.browser_wrapper import BrowserWrapper
from infra.jira_handler import JiraHandler
from infra.json_file_handler import JsonFileHandler
from infra.logger import Logger
from infra.utilities import Utilities
from logic.UI.contact_page import ContactPage
from logic.UI.home_page import HomePage


class TestContactPageUI(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        self._config = JsonFileHandler().load_from_file('../../demo_blaze_config.json', __file__)
        self._logger = Logger().get_logger()
        self._error = None  # This is used to detect the assertion failed for the jira report

    def tearDown(self):
        if self._error:
            try:
                issue_description = JiraHandler().issue_description(self._error, self._testMethodName)
                (JiraHandler().create_issue
                 (self._config["jira_project_key"], issue_description, "An error occurred during the test"))
            except Exception as e:
                self._logger.error(f"The Reporting to jira failed : {e}")
        self._driver.quit()

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
        contact_page.insert_contact_email(Utilities().generate_random_email(self._config["email_host"]))
        contact_page.insert_contact_name(Utilities().generate_username(8))
        contact_page.insert_contact_message(Utilities().generate_paragraph(1,20))
        contact_page.click_send_message()

        # Assert the alert message after sending
        self.assertEqual(self._config["contact_message_success"], contact_page.get_alert_text(self._driver))

    def test_send_empty_contact_message(self):
        """
            Test Case 023: Validate that an appropriate error alert message is displayed when attempting to send a
            contact message with empty fields.
        """
        # Pre-conditions
        home_page = HomePage(self._driver)

        # Navigate to the contact page and send empty message
        home_page.click_contact_button()
        contact_page = ContactPage(self._driver)
        contact_page.click_send_message()

        try:
            # Assert the alert message
            self.assertEqual(self._config["contact_message_error"], contact_page.get_alert_text(self._driver))
        except AssertionError as e:
            self._error = f"The Assertion Failed : {e}"
            raise
