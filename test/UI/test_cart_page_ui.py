import os
import unittest
from infra.UI.browser_wrapper import BrowserWrapper
from infra.json_file_handler import JsonFileHandler


class TestCartPageUI(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)

    def tearDown(self):
        self._driver.quit()
