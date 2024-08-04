from selenium.webdriver.common.by import By

from logic.UI.app_base_page import AppBasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage(AppBasePage):
    ADD_TO_CART = "//a[@onclick='addToCart(9)']"
    PRODUCT_NAME = "//h2[@class='name']"
    PRODUCT_PRICE = "//h3[@class='price-container']"
    PRODUCT_DESCRIPTION_TITLE = "//div[@id='more-information']/strong"
    PRODUCT_DESCRIPTION = "//div[@id='more-information']/p"
    PRODUCT_IMAGE = "//div[@class='item active']/img"

    def __init__(self, driver):
        super().__init__(driver)
        self._add_to_cart_locator = (By.XPATH, self.ADD_TO_CART)
        self._product_name_locator = (By.XPATH, self.PRODUCT_NAME)
        self._product_price_locator = (By.XPATH, self.PRODUCT_PRICE)
        self._product_description_title_locator = (By.XPATH, self.PRODUCT_DESCRIPTION_TITLE)
        self._product_description_locator = (By.XPATH, self.PRODUCT_DESCRIPTION)
        self._product_image_locator = (By.XPATH, self.PRODUCT_IMAGE)
