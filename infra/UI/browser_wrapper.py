from selenium import webdriver
from infra.custom_exception import CustomException
from infra.json_file_handler import JsonFileHandler


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self._config = JsonFileHandler.load_from_file('../../demo_blaze_config.json')

    def get_driver(self):
        url = self._config.get("url")
        if not url:
            raise ValueError("URL not found in the configuration.")
        try:
            if self._config["browser"] == "Chrome":
                self._driver = webdriver.Chrome()
            elif self._config["browser"] == "FireFox":
                self._driver = webdriver.Firefox()
            elif self._config["browser"] == "Edge":
                self._driver = webdriver.Edge()
        except Exception as e:
            raise CustomException(f"Browser loading error check browser if supported: {e}")

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
