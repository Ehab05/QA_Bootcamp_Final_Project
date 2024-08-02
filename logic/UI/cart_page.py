from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.UI.base_page import BasePage


class CartPage(BasePage):
    TOTAL_AMOUNT = "//div[@class='panel-heading']"
    PLACE_ORDER_BUTTON = "//div[@class='col-lg-1']/button"
    PRODUCTS_LIST = "//tbody[@id='tbodyid']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._total_amount_locator = (By.XPATH, self.TOTAL_AMOUNT)
        self._place_order_button_locator = (By.XPATH, self.PLACE_ORDER_BUTTON)
        self._products_list_locator = (By.XPATH, self.PRODUCTS_LIST)

    def get_total_amount(self):
        total_amount = (WebDriverWait(self._driver, 10).until
                        (EC.visibility_of_element_located(self._total_amount_locator)))
        return total_amount.text

    def place_order_button(self):
        place_order_button = (WebDriverWait(self._driver, 10).until
                              (EC.visibility_of_element_located(self._place_order_button_locator)))
        place_order_button.click()

    def get_product_list(self):
        products_list = (WebDriverWait(self._driver, 10).until
                         (EC.visibility_of_element_located(self._products_list_locator)))



# from infra.utilities import Utilities
#
# password = "123456"
# encoded_password = Utilities().encode_password(password)
# print(f"Base64 Encoded Password: {encoded_password}")
# print(Utilities().generate_random_credit_card("visa"))
