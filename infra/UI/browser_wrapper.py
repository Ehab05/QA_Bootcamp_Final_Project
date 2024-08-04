from selenium import webdriver
from infra.custom_exception import CustomException
from infra.json_file_handler import JsonFileHandler


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self.config = JsonFileHandler.load_from_file('../../demo_blaze_config.json')

    def get_driver(self):
        url = self.config.get("url")
        if not url:
            raise ValueError("URL not found in the configuration.")
        try:
            if self.config["browser"] == "Chrome":
                self._driver = webdriver.Chrome()
            elif self.config["browser"] == "FireFox":
                self._driver = webdriver.Firefox()
            elif self.config["browser"] == "Edge":
                self._driver = webdriver.Edge()
        except Exception as e:
            raise CustomException(f"Browser loading error check browser if supported: {e}")

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
