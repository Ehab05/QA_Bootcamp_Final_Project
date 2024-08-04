import json
import os
from infra.API.api_wrapper import APIWrapper
from infra.custom_exception import CustomException
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
        self._logger = Logger('demo_blaze.log').get_logger()

    def login(self):
        try:
            login_body = {"username": "g1g1g1", "password": "MTIzNDU2"}
            response = self._request.post_request(self._url, login_body)
            return response
        except Exception as e:
            self._logger.error(f"Error logging in: {e}")
            return None

    def convert_to_dict(self, text):
        try:
            text = text.strip()
            # Split the input string at the colon
            key, value = text.split(':', 1)
            # Strip leading/trailing whitespace from key and value
            key = key.strip().strip('"')
            value = value.strip().strip('"')
            # Create a dictionary
            result_dict = {key: value}

            return result_dict
        except:
            raise CustomException(f"Invalid text format")

    def extract_auth_token(self, response_text):
        # Split the response text using 'Auth_token:' and clean up
        response_dict = self.convert_to_dict(response_text)
        token = response_dict["Auth_token"]
        return token

    def check_token(self, token):
        try:
            """Check if the token is valid."""
            url = "https://api.demoblaze.com/check"
            headers = {
                "Authorization": f"Bearer {token}"
            }
            response = self._request.post_request(url, body={"token": "ZzFnMWcxMTcyMzIyOA=="}, headers=headers)
            return response.data
        except:
            raise CustomException(f"Auth_token not found in the response text")
