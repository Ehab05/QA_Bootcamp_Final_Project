import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from infra.json_file_handler import JsonFileHandler
from logic.UI.app_base_page import AppBasePage


class LoginPage(AppBasePage):
    USER_NAME_INPUT = "//input[@id='loginusername']"
    PASSWORD_INPUT = "//input[@id='loginpassword']"
    CLOSE_BUTTON = "//div[@id='logInModal']//button[@class='btn btn-secondary']"
    LOG_IN_BUTTON = "//button[@onclick='logIn()']"
    X_BUTTON = "//div[@id='logInModal']//button[@class='close']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._user_name_input_locator = (By.XPATH, self.USER_NAME_INPUT)
        self._password_input_locator = (By.XPATH, self.PASSWORD_INPUT)
        self._close_button_locator = (By.XPATH, self.CLOSE_BUTTON)
        self._log_in_button_locator = (By.XPATH, self.LOG_IN_BUTTON)
        self._x_button_locator = (By.XPATH, self.X_BUTTON)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)

    def insert_username(self, username):
        user_name_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._user_name_input_locator))
        user_name_input.send_keys(username)

    def clear_username_input_field(self):
        user_name_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._user_name_input_locator))
        user_name_input.clear()

    def insert_password(self, password):
        password_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._password_input_locator))
        password_input.send_keys(password)

    def clear_password_input_field(self):
        password_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._password_input_locator))
        password_input.clear()

    def click_close_button(self):
        close_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._close_button_locator))
        close_button.click()

    def click_x_button(self):
        x_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._x_button_locator))
        x_button.click()

    def click_login_button(self):
        log_in_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._log_in_button_locator))
        log_in_button.click()

    def get_login_missing_fields_message(self):
        return self._config["missing_fields_message"]

    def get_invalid_password_message(self):
        return self._config["login_password_error_message"]

    def login_flow(self):
        self.insert_username(self._config["username"])
        self.insert_password(self._config["password"])
        self.click_login_button()


