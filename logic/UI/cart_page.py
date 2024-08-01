from infra.UI.base_page import BasePage


class CartPage(BasePage):
    TOTAL_AMOUNT = "//div[@class='panel-heading']"
    PLACE_ORDER_BUTTON = "//div[@class='col-lg-1']/button"
    PRODUCTS_LIST = "//tbody[@id='tbodyid']"

    def __init__(self, driver):
        super().__init__(driver)

# from infra.utilities import Utilities
#
# password = "123456"
# encoded_password = Utilities().encode_password(password)
# print(f"Base64 Encoded Password: {encoded_password}")
# print(Utilities().generate_random_credit_card("visa"))
