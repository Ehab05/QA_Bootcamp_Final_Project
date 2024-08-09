import os
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.json_file_handler import JsonFileHandler
from infra.logger import Logger
from infra.utilities import Utilities
from logic.UI.app_base_page import AppBasePage


class HomePage(AppBasePage):
    CATEGORIES_PHONES_BUTTON = "//a[@onclick=\"byCat('phone')\"]"
    CATEGORIES_LAPTOPS_BUTTON = "//a[@onclick=\"byCat('notebook')\"]"
    CATEGORIES_MONITORS_BUTTON = "//a[@onclick=\"byCat('monitor')\"]"
    PREVIOUS_BUTTON = "//button[@id='prev2']"
    NEXT_BUTTON = "//button[@id='next2']"
    CAROUSEL_NEXT_BUTTON = "//a[@class='carousel-control-next']"
    CAROUSEL_PREV_BUTTON = "//a[@class='carousel-control-prev']"
    STORE_PRODUCT = "//a[contains(text() ,f"'{product_name}'")]"
    PRODUCT_LIST = "//div[@id='tbodyid']/div[@class='col-lg-4 col-md-6 mb-4']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._phones_button_locator = (By.XPATH, self.CATEGORIES_PHONES_BUTTON)
        self._laptops_button_locator = (By.XPATH, self.CATEGORIES_LAPTOPS_BUTTON)
        self._monitors_button_locator = (By.XPATH, self.CATEGORIES_MONITORS_BUTTON)
        self._previous_button_locator = (By.XPATH, self.PREVIOUS_BUTTON)
        self._next_button_locator = (By.XPATH, self.NEXT_BUTTON)
        self._carousel_next_button_locator = (By.XPATH, self.CAROUSEL_NEXT_BUTTON)
        self._carousel_prev_button_locator = (By.XPATH, self.CAROUSEL_PREV_BUTTON)
        self._products_list_locator = (By.XPATH, self.PRODUCT_LIST)
        self._products_list_data = []
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)
        self._logger = Logger().get_logger()

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
        Utilities().retry_waiting_for_element_to_click(3, self._driver, self.NEXT_BUTTON)

    def click_carousel_next_button(self):
        next_button = (WebDriverWait(self._driver, 5).until
                       (EC.visibility_of_element_located(self._carousel_next_button_locator)))
        next_button.click()

    def click_carousel_previous_button(self):
        prev_button = (WebDriverWait(self._driver, 5).until
                       (EC.visibility_of_element_located(self._carousel_prev_button_locator)))
        prev_button.click()

    def click_on_product_by_name(self, product_name):
        product_path = f"//a[contains(text(), '{product_name}')]"
        Utilities().retry_waiting_for_element_to_click(3, self._driver, product_path)

    def get_product_list_from_home_page(self):
        time.sleep(1)
        products_list = (WebDriverWait(self._driver, 10).until
                         (EC.visibility_of_all_elements_located(self._products_list_locator)))
        for product in products_list:
            image_src = product.find_element(By.TAG_NAME, "img").get_attribute("src")
            title_link = product.find_element(By.CLASS_NAME, "hrefch")
            title = title_link.text
            price = product.find_element(By.TAG_NAME, "h5").text
            description = product.find_element(By.TAG_NAME, "p").text
            self._products_list_data.append({
                'image': image_src,
                'title': title,
                'title_link': title_link,
                'price': price,
                'description': description
            })

    def get_login_success_message(self):
        success_message = "Welcome " + self._config["username"]
        return success_message

    def get_product_list(self):
        return self._products_list_data

    def get_random_product_title(self):
        # Extract titles from the product list
        self.get_product_list_from_home_page()
        titles = list(map(lambda product: product['title'], self.get_product_list()))
        title = random.choice(titles)
        self._logger.info(f"This is the product title that was generated: {title}")

        # Return a random title from the list
        return title
