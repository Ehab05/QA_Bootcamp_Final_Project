from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.UI.app_base_page import AppBasePage


class CartPage(AppBasePage):
    TOTAL_AMOUNT = "//div[@class='panel-heading']"
    PLACE_ORDER_BUTTON = "//div[@class='col-lg-1']/button"
    PRODUCTS_LIST = "#tbodyid tr"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._total_amount_locator = (By.XPATH, self.TOTAL_AMOUNT)
        self._place_order_button_locator = (By.XPATH, self.PLACE_ORDER_BUTTON)
        self._products_list_locator = (By.CSS_SELECTOR, self.PRODUCTS_LIST)
        self._products_data = []

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
                         (EC.visibility_of_all_elements_located(self._products_list_locator)))
        for product in products_list:
            cells = product.find_elements(By.TAG_NAME, "td")
            image_src = cells[0].find_element(By.TAG_NAME, "img").get_attribute("src")
            title = cells[1].text
            price = cells[2].text
            delete_link = cells[3].find_element(By.TAG_NAME, "a")
            self._products_data.append({
                'Image': image_src,
                'Title': title,
                'Price': price,
                'Delete Link': delete_link
            })







