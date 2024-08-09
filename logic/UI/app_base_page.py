import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from infra.UI.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from infra.custom_exception import CustomException


class AppBasePage(BasePage):
    PRODUCT_STORE_BUTTON = "//a[@id='nava']"
    HOME_BUTTON = "//li[@class='nav-item active']//a[@class='nav-link']"
    CONTACT_BUTTON = "//li[@class='nav-item']//a[@data-target='#exampleModal']"
    ABOUT_US_BUTTON = "//li[@class='nav-item']//a[@data-target='#videoModal']"
    CART_BUTTON = "//a[@id='cartur']"
    LOGIN_BUTTON = "//a[@id='login2']"
    SIGN_UP_BUTTON = "//a[@id='signin2']"
    LOGOUT_BUTTON = "//a[@id='logout2']"
    NAME_OF_USER = "//a[@id='nameofuser']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._product_store_button_locator = (By.XPATH, self.PRODUCT_STORE_BUTTON)
        self._home_button_locator = (By.XPATH, self.HOME_BUTTON)
        self._contact_button_locator = (By.XPATH, self.CONTACT_BUTTON)
        self._about_us_button_locator = (By.XPATH, self.ABOUT_US_BUTTON)
        self._cart_button_locator = (By.XPATH, self.CART_BUTTON)
        self._login_button_locator = (By.XPATH, self.LOGIN_BUTTON)
        self._sign_up_button_locator = (By.XPATH, self.SIGN_UP_BUTTON)
        self._logout_button_locator = (By.XPATH, self.LOGOUT_BUTTON)
        self._name_of_user_locator = (By.XPATH, self.NAME_OF_USER)

    def click_product_store_button(self):
        product_store_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._product_store_button_locator))
        product_store_button.click()

    def click_home_button(self):
        home_button = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self._home_button_locator))
        home_button.click()

    def click_contact_button(self):
        contact_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._contact_button_locator))
        contact_button.click()

    def click_about_us_button(self):
        about_us_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._about_us_button_locator))
        about_us_button.click()

    def click_cart_button(self):
        cart_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._cart_button_locator))
        cart_button.click()

    def click_login_button(self):
        login_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._login_button_locator))
        login_button.click()

    def get_login_button_text(self):
        login_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._login_button_locator))
        return login_button.text

    def click_sign_up_button(self):
        sign_up_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._sign_up_button_locator))
        sign_up_button.click()

    def get_sign_up_button_text(self):
        sign_up_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._sign_up_button_locator))
        return sign_up_button.text

    def click_logout_button(self):
        logout_button = WebDriverWait(self._driver, 12).until(
            EC.element_to_be_clickable(self._logout_button_locator))
        logout_button.click()

    def get_name_of_user(self):
        name_of_user = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(self._name_of_user_locator))
        return name_of_user.text

    def get_alert_text(self, driver):
        try:
            # Wait for the alert to be present

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

    def accept_alert(self):
        alert = WebDriverWait(self._driver, 10).until(EC.alert_is_present())
        alert.accept()
