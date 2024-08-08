import os
from infra.API.api_wrapper import APIWrapper
from infra.custom_exception import CustomException
from infra.json_file_handler import JsonFileHandler
from infra.logger import Logger
from infra.utilities import Utilities
from logic.utilities_logic import UtilitiesLogic


class APILoginPage:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._url = UtilitiesLogic().get_url_with_endpoint("login")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(config_file_path)
        self._logger = Logger('demo_blaze.log').get_logger()

    def login_via_api(self, username, password):
        try:

            login_body = {"username": username, "password": password}
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

    def get_token_from_response(self, response):
        auth_token = self.extract_auth_token(response.text)
        self._request.set_auth_token(auth_token)
        return {'name': 'tokenp_', 'value': auth_token, 'path': '/'}

    def check_auth_token(self, auth_token):
        auth_token = self.convert_to_dict(auth_token)
        return auth_token

    def get_username_and_password(self):
        username = self._config.get("username")
        password = Utilities().encode_password_by_base64(self._config.get("password"))
        return username, password

    def login_flow_through_api(self):
        login_api = APILoginPage(self._request)
        username, password = login_api.get_username_and_password()
        response = login_api.login_via_api(username, password)
        token = login_api.get_token_from_response(response)
        return token


