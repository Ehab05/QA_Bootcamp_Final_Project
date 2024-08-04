from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from infra.UI.base_page import BasePage


class SignupPage(BasePage):
    USER_NAME_INPUT = "//input[@id='loginusername']"
    PASSWORD_INPUT = "//input[@id='loginpassword']"
    CLOSE_BUTTON = "//div[@id='logInModal']//button[@class='btn btn-secondary']"
    LOG_IN_BUTTON = "//button[@onclick='logIn()']"
    X_BUTTON = "//div[@id='logInModal']//button[@class='close']"

    def __init__(self, driver):
        super().__init__(driver)
        self._user_name_input_locator = (By.XPATH, self.USER_NAME_INPUT)
        self._password_input_locator = (By.XPATH, self.PASSWORD_INPUT)
        self._close_button_locator = (By.XPATH, self.CLOSE_BUTTON)
        self._log_in_button_locator = (By.XPATH, self.LOG_IN_BUTTON)
        self._x_button_locator = (By.XPATH, self.X_BUTTON)

    def insert_username(self, username):
        user_name_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._user_name_input_locator))
        user_name_input.send_keys(username)

    def insert_password(self, password):
        password_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._password_input_locator))
        password_input.send_keys(password)

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

