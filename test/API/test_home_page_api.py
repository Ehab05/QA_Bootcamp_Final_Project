import os
import unittest

from infra.API.api_wrapper import APIWrapper
from infra.json_file_handler import JsonFileHandler
from logic.API.API_login_page import APILoginPage


class TestHomeAPIPage(unittest.TestCase):
    def setUp(self):
        self._request = APIWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)



