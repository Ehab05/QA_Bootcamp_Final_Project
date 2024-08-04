from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.UI.base_page import BasePage


class ContactPage(BasePage):
    CONTACT_EMAIL_INPUT = "//input[@id='recipient-email']"
    CONTACT_NAME_INPUT = "//input[@id='recipient-name']"
    CONTACT_MESSAGE_INPUT = "//textarea[@id='message-text']"
    CLOSE_BUTTON = "//div[@id='exampleModal']//button[@class='btn btn-secondary']"
    X_BUTTON = "//div[@id='exampleModal']//button[@class='close']"
    SEND_MESSAGE_BUTTON = "//button[@onclick='send()']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._contact_email_input_locator = (By.XPATH, self.CONTACT_EMAIL_INPUT)
        self._contact_name_input_locator = (By.XPATH, self.CONTACT_NAME_INPUT)
        self._contact_message_input_locator = (By.XPATH, self.CONTACT_MESSAGE_INPUT)
        self._close_button_locator = (By.XPATH, self.CLOSE_BUTTON)
        self._x_button_locator = (By.XPATH, self.X_BUTTON)
        self._send_message_button_locator = (By.XPATH, self.SEND_MESSAGE_BUTTON)

    def insert_contact_email(self, contact_email):
        email_input = (WebDriverWait(self._driver, 10).until
                       (EC.visibility_of_element_located(self._contact_email_input_locator)))
        email_input.send_keys(contact_email)

    def insert_contact_name(self, contact_name):
        name_input = (WebDriverWait(self._driver, 10).until
                      (EC.visibility_of_element_located(self._contact_name_input_locator)))
        name_input.send_keys(contact_name)

    def insert_contact_message(self, contact_message):
        message = (WebDriverWait(self._driver, 10).until
                   (EC.visibility_of_element_located(self._contact_message_input_locator)))
        message.send_keys(contact_message)

    def click_x_button(self):
        x_button = (WebDriverWait(self._driver, 10).until
                    (EC.visibility_of_element_located(self._x_button_locator)))
        x_button.click()

    def click_close_button(self):
        close_button = (WebDriverWait(self._driver, 10).until
                        (EC.visibility_of_element_located(self._close_button_locator)))
        close_button.click()

    def click_send_message(self):
        send_message_button = (WebDriverWait(self._driver, 10).until
                               (EC.visibility_of_element_located(self._send_message_button_locator)))
        send_message_button.click()
        
