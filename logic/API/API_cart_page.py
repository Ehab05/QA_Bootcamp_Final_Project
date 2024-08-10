import os
from selenium.webdriver.chrome.webdriver import WebDriver
from infra.API.api_wrapper import APIWrapper
from infra.json_file_handler import JsonFileHandler
from infra.utilities import Utilities
from logic.utilities_logic import UtilitiesLogic


class APICartPage:
    def __init__(self, request: APIWrapper):
        self._request = request
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(config_file_path)

    def view_cart_with_registered_user_via_api(self, token):
        url = UtilitiesLogic().get_url_with_endpoint("viewcart")
        response = self._request.post_request(url, {
            "cookie": token,
            "flag": "true"
        })
        return response

    def view_cart_with_unregistered_user_via_api(self, driver: WebDriver):

        cookies = Utilities().wait_for_action(driver.get_cookies, 1, 3)
        # Use filter to find the 'user' cookie
        user_cookie = list(filter(lambda c: c['name'] == 'user', cookies))
        cookie_value = user_cookie[0]['value']
        url = UtilitiesLogic().get_url_with_endpoint("viewcart")
        false = False
        response = self._request.post_request(url, {
            "cookie": cookie_value,
            "flag": false
        })

        return response

    def get_entry(self):
        url = UtilitiesLogic().get_url_with_endpoint("entries")
        entries = self._request.get_request(url)
        return entries.cookies

    def add_item_to_cart(self):
        url = UtilitiesLogic().get_url_with_endpoint("addtocart")
        cookies = self._request.get_cookies()
        print(cookies)
        response = self._request.post_request(url, cookies)
        return response
