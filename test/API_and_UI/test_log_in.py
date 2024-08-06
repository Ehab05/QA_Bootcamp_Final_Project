import unittest

from infra.API.api_wrapper import APIWrapper
from infra.UI.browser_wrapper import BrowserWrapper
from logic.API.API_login_page import APILogin
from logic.UI.home_page import HomePage


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self._request = APIWrapper()
        self._driver = BrowserWrapper().get_driver()

    def tearDown(self):
        pass

    def test_login_api(self):
        """
            Test Case 013: Ensure that a user can log in via API, add the authentication token to the browser's cookies,
            and verify the welcome message on the web UI.
        """
        # Initialize login api page
        login_api = APILogin(self._request)
        username, password = login_api.get_username_and_password()

        # Send post request to the api
        response = login_api.login_via_api(username, password)

        # Update the page cookie with the token
        token = login_api.get_token_from_response(response)
        home_page = HomePage(self._driver)
        home_page.add_token_to_cookie(token)

        # Assert the welcome message via the UI
        self.assertEqual(home_page.get_login_success_message(), home_page.get_name_of_user())

