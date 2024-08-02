from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.UI.base_page import BasePage


class HomePage(BasePage):
    CATEGORIES_PHONES_BUTTON = "//a[@onclick=\"byCat('phone')\"]"
    CATEGORIES_LAPTOPS_BUTTON = "//a[@onclick=\"byCat('notebook')\"]"
    CATEGORIES_MONITORS_BUTTON = "//a[@onclick=\"byCat('monitor')\"]"
    PREVIOUS_BUTTON = "//button[@id='prev2']"
    NEXT_BUTTON = "//button[@id='next2']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._phones_button_locator = (By.XPATH, self.CATEGORIES_PHONES_BUTTON)
        self._laptops_button_locator = (By.XPATH, self.CATEGORIES_LAPTOPS_BUTTON)
        self._monitors_button_locator = (By.XPATH, self.CATEGORIES_MONITORS_BUTTON)
        self._previous_button_locator = (By.XPATH, self.PREVIOUS_BUTTON)
        self._next_button_locator = (By.XPATH, self.NEXT_BUTTON)

    def click_phones_button(self):
        phones_button = (WebDriverWait(self._driver, 10).until
                         (EC.visibility_of_element_located(self._phones_button_locator)))
        phones_button.click()

    def click_laptops_button(self):
        laptops_button = (WebDriverWait(self._driver, 10).until
                          (EC.visibility_of_element_located(self._laptops_button_locator)))
        laptops_button.click()

    def click_monitors_button(self):
        monitors_button = (WebDriverWait(self._driver, 10).until
                           (EC.visibility_of_element_located(self._monitors_button_locator)))
        monitors_button.click()

    def click_previous_button(self):
        previous_button = (WebDriverWait(self._driver, 10).until
                           (EC.visibility_of_element_located(self._previous_button_locator)))
        previous_button.click()

    def click_next_button(self):
        next_button = (WebDriverWait(self._driver, 10).until
                       (EC.visibility_of_element_located(self._next_button_locator)))
        next_button.click()
