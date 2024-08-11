import os
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.API.api_wrapper import APIWrapper
from infra.custom_exception import CustomException
from infra.json_file_handler import JsonFileHandler
from infra.logger import Logger
from infra.utilities import Utilities
from logic.utilities_logic import UtilitiesLogic


class APISignUpPage:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._url = UtilitiesLogic().get_url_with_endpoint("signup")
        self._config = JsonFileHandler().load_from_file('../../demo_blaze_config.json', __file__)
        self._logger = Logger().get_logger()

    def sign_up(self, username, password):
        try:
            encoded_password = Utilities().encode_password_by_base64(password)
            sign_up_body = {"username": username, "password": encoded_password}
            response = self._request.post_request(self._url, sign_up_body)
            self._config["username"] = username
            self._config["password"] = password
            JsonFileHandler().save_to_file('../../demo_blaze_config.json', __file__)
            return response
        except Exception as e:
            self._logger.error(f"Error signing up: {e}")
            return None

    def get_alert_text(self, driver):
        try:
            # Wait for the alert to be present
            driver.refresh()
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            # Switch to the alert
            alert = Alert(driver)
            # Get the alert text
            alert_text = alert.text
            # Accept the alert
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            raise CustomException(f"Alert presence error")

    def get_config(self):
        return self._config



