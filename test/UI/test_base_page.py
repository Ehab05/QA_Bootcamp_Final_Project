import json
import time
import unittest

import requests
from selenium.webdriver.common.alert import Alert

from infra.API.api_wrapper import APIWrapper
from infra.UI.browser_wrapper import BrowserWrapper
from logic.API.login import Login
from logic.UI.home_page import HomePage
from logic.UI.login_page import LoginPage


class TestBasePage(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        self._request = APIWrapper()

    def tearDown(self):
        self._driver.quit()

    def test_login_page(self):
        home_page = HomePage(self._driver)
        home_page.click_login_button()
        login_page = LoginPage(self._driver)

        login_page.insert_username("g1g1g1")
        login_page.insert_password("123456")
        login_page.click_login_button()
        home_page = HomePage(self._driver)
        logged_in_user_message = home_page.get_name_of_user()

        self.assertEqual("Welcome g1g1g1", logged_in_user_message)

    def test_login_api(self):
        login_api = Login(self._request)
        response = login_api.login()
        auth_token = login_api.extract_auth_token(response.text)
        self._request.set_auth_token(auth_token)
        self._driver.add_cookie({'name': 'tokenp_', 'value': auth_token, 'path': '/'})
        self._driver.refresh()
        check_response = login_api.check_token(auth_token)
        self.assertEqual(check_response["Item"]["username"], "g1g1g1")
        home_page = HomePage(self._driver)
        self.assertIsNotNone(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Welcome g1g1g1", home_page.get_name_of_user())
