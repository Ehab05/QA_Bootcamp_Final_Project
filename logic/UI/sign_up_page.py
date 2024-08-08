import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from infra.json_file_handler import JsonFileHandler
from logic.UI.app_base_page import AppBasePage


class SignUpPage(AppBasePage):
    USER_NAME_INPUT = "//input[@id='sign-username']"
    PASSWORD_INPUT = "//input[@id='sign-password']"
    CLOSE_BUTTON = "//div[@id='logInModal']//button[@class='btn btn-secondary']"
    SIGN_UP_BUTTON = "//button[@onclick='register()']"
    X_BUTTON = "//div[@id='logInModal']//button[@class='close']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)
        self._user_name_input_locator = (By.XPATH, self.USER_NAME_INPUT)
        self._password_input_locator = (By.XPATH, self.PASSWORD_INPUT)
        self._close_button_locator = (By.XPATH, self.CLOSE_BUTTON)
        self._sign_up_button_locator = (By.XPATH, self.SIGN_UP_BUTTON)
        self._x_button_locator = (By.XPATH, self.X_BUTTON)

    def insert_username(self, username):
        user_name_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._user_name_input_locator))
        user_name_input.send_keys(username)
        self._config["username"] = username
        JsonFileHandler().save_to_file(self._config_file_path, self._config)

    def clear_username_input_field(self):
        user_name_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._user_name_input_locator))
        user_name_input.clear()

    def insert_password(self, password):
        password_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._password_input_locator))
        password_input.send_keys(password)
        self._config["password"] = password
        JsonFileHandler().save_to_file(self._config_file_path, self._config)

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

    def click_sign_up_button(self):
        sign_up_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._sign_up_button_locator))
        sign_up_button.click()

    def get_success_signup_message(self):
        return self._config["signup_success_message"]

    def get_signup_missing_fields_message(self):
        return self._config["missing_fields_message"]
