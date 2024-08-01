from infra.UI.base_page import BasePage


class HomePage(BasePage):
    CATEGORIES_PHONES_BUTTON = "//a[@onclick=\"byCat('phone')\"]"
    CATEGORIES_LAPTOPS_BUTTON = "//a[@onclick=\"byCat('notebook')\"]"
    CATEGORIES_MONITORS_BUTTON = "//a[@onclick=\"byCat('monitor')\"]"
    PREVIOUS_BUTTON = "//button[@id='prev2']"
    NEXT_BUTTON = "//button[@id='next2']"

    def __init__(self, driver):
        super().__init__(driver)
