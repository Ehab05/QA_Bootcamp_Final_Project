import os

from infra.API.api_wrapper import APIWrapper
from infra.json_file_handler import JsonFileHandler
from logic.utilities_logic import UtilitiesLogic


class APIHomePage:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._url = UtilitiesLogic().get_url_with_endpoint("")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(config_file_path)
