import os
import re

from infra.API.api_wrapper import APIWrapper
from infra.json_file_handler import JsonFileHandler
from infra.logger import Logger
from logic.utilities_logic import UtilitiesLogic


class Login:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._url = UtilitiesLogic().get_url_with_endpoint("login")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(config_file_path)
        self._logger = Logger("fake_rest_api.log").get_logger()

    def login(self):
        try:
            login_body = {"username": "g1g1g1", "password": "MTIzNDU2"}
            response = self._request.post_request(self._url, login_body)
            return response
        except Exception as e:
            self._logger.error(f"Error logging in: {e}")
            return None

    def extract_auth_token(self, response_text):
        # Split the response text using 'Auth_token:' and clean up
        parts = response_text.split('Auth_token:')

        if len(parts) > 1:
            # Extract the part after 'Auth_token:', and remove leading/trailing whitespace
            token = parts[1].strip().strip('"')
            return token

        return None

    def check_token(self, token):
        """Check if the token is valid."""
        url = "https://api.demoblaze.com/check"
        headers = {
            "Authorization": f"Bearer {token}",
        #     "Content-Type": "application/json",
        #     "Accept": "*/*",
        #     "Origin": "https://www.demoblaze.com",
        #     "Referer": "https://www.demoblaze.com/",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
         }
        response = self._request.post_request(url, body={"token": "ZzFnMWcxMTcyMzIyOA=="}, headers=headers)
        return response.data
