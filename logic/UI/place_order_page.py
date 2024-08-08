from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.UI.app_base_page import AppBasePage


class PlaceOrderPage(AppBasePage):
    PAGE_TITLE = "//h5[@id='orderModalLabel']"
    TOTAL_AMOUNT = "//label[@id='totalm']"
    NAME_INPUT = "//input[@id='name']"
    COUNTRY_INPUT = "//input[@id='country']"
    CITY_INPUT = "//input[@id='city']"
    CARD_INPUT = "//input[@id='card']"
    MONTH_INPUT = "//input[@id='month']"
    YEAR_INPUT = "//input[@id='year']"
    X_BUTTON = "//div[@id='orderModal']//button[@class='close']"
    CLOSE_BUTTON = "//div[@id='orderModal']//button[@class='btn btn-secondary']"
    PURCHASE_BUTTON = "//button[@onclick='purchaseOrder()']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._page_title_locator = (By.XPATH, self.PAGE_TITLE)
        self._total_amount_locator = (By.XPATH, self.TOTAL_AMOUNT)
        self._name_input_locator = (By.XPATH, self.NAME_INPUT)
        self._country_input_locator = (By.XPATH, self.COUNTRY_INPUT)
        self._city_input_locator = (By.XPATH, self.CITY_INPUT)
        self._card_input_locator = (By.XPATH, self.CARD_INPUT)
        self._month_input_locator = (By.XPATH, self.MONTH_INPUT)
        self._year_input_locator = (By.XPATH, self.YEAR_INPUT)
        self._x_button_locator = (By.XPATH, self.X_BUTTON)
        self._close_button_locator = (By.XPATH, self.CLOSE_BUTTON)
        self._purchase_button_locator = (By.XPATH, self.PURCHASE_BUTTON)

    def get_page_title(self):
        page_title = (WebDriverWait(self._driver, 5).until
                      (EC.visibility_of_element_located(self._page_title_locator)))
        return page_title.text

    def get_total_amount(self):
        total_amount = (WebDriverWait(self._driver, 5).until
                        (EC.visibility_of_element_located(self._total_amount_locator)))
        return total_amount.text

    def insert_name_input(self, name):
        name_input = (WebDriverWait(self._driver, 5).until
                      (EC.visibility_of_element_located(self._name_input_locator)))
        name_input.clear()
        name_input.send_keys(name)

    def insert_country_input(self, country):
        country_input = (WebDriverWait(self._driver, 5).until
                         (EC.visibility_of_element_located(self._country_input_locator)))
        country_input.clear()
        country_input.send_keys(country)

    def insert_city_input(self, city):
        city_input = (WebDriverWait(self._driver, 5).until
                      (EC.visibility_of_element_located(self._city_input_locator)))
        city_input.clear()
        city_input.send_keys(city)

    def insert_card_number_input(self, card):
        card_input = (WebDriverWait(self._driver, 5).until
                      (EC.visibility_of_element_located(self._card_input_locator)))
        card_input.clear()
        card_input.send_keys(card)

    def insert_month_input(self, month):
        month_input = (WebDriverWait(self._driver, 5).until
                       (EC.visibility_of_element_located(self._month_input_locator)))
        month_input.clear()
        month_input.send_keys(month)

    def insert_year_input(self, year):
        year_input = (WebDriverWait(self._driver, 5).until
                      (EC.visibility_of_element_located(self._year_input_locator)))
        year_input.clear()
        year_input.send_keys(year)

    def click_x_button(self):
        x_button = (WebDriverWait(self._driver, 5).until
                    (EC.visibility_of_element_located(self._x_button_locator)))
        x_button.click()

    def click_close_button(self):
        close_button = (WebDriverWait(self._driver, 5).until
                        (EC.visibility_of_element_located(self._close_button_locator)))
        close_button.click()

    def click_purchase_button(self):
        purchase_button = (WebDriverWait(self._driver, 5).until
                           (EC.visibility_of_element_located(self._purchase_button_locator)))
        purchase_button.click()
