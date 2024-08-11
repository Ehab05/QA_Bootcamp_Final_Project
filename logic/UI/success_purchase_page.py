from selenium.webdriver.common.by import By
from logic.UI.app_base_page import AppBasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SuccessPurchasePage(AppBasePage):
    PURCHASE_SUCCESS_MESSAGE = "//div[@class='sweet-alert  showSweetAlert visible']/h2"
    OK_BUTTON = "//button[@class='confirm btn btn-lg btn-primary']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._purchase_success_message_locator = (By.XPATH, self.PURCHASE_SUCCESS_MESSAGE)
        self._ok_button_locator = (By.XPATH, self.OK_BUTTON)

    def get_purchase_success_message(self):
        message = (WebDriverWait(self._driver, 10).until
                   (EC.visibility_of_element_located(self._purchase_success_message_locator)))
        return message.text

    def click_ok_button(self):
        ok_button = (WebDriverWait(self._driver, 10).until
                     (EC.visibility_of_element_located(self._ok_button_locator)))
        ok_button.click()
