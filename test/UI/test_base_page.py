import os
import time
import unittest
from infra.API.api_wrapper import APIWrapper
from infra.UI.browser_wrapper import BrowserWrapper
from infra.json_file_handler import JsonFileHandler
from infra.utilities import Utilities
from logic.API.login import Login
from logic.UI.about_us_page import AboutUsPage
from logic.UI.home_page import HomePage
from logic.UI.login_page import LoginPage
from logic.UI.sign_up_page import SignUpPage


class TestBasePage(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        self._request = APIWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)

    def tearDown(self):
        self._driver.quit()

    def test_login_page(self):
        home_page = HomePage(self._driver)
        home_page.click_login_button()
        login_page = LoginPage(self._driver)

        login_page.insert_username("g1g1g1")
        login_page.insert_password("123456")
        login_page.click_login_button()
        home_page = HomePage(self._driver)
        logged_in_user_message = home_page.get_name_of_user()

        self.assertEqual("Welcome g1g1g1", logged_in_user_message)

    def test_login_api(self):
        login_api = Login(self._request)
        response = login_api.login(self._driver)
        home_page = HomePage(response)
        self.assertEqual("Welcome g1g1g1", home_page.get_name_of_user())

    def test_valid_sign_up(self):
        home_page = HomePage(self._driver)
        home_page.click_sign_up_button()
        sing_up_page = SignUpPage(self._driver)
        sing_up_page.insert_username(Utilities().generate_username(8))
        sing_up_page.insert_password(Utilities().generate_random_passwrod(8))
        sing_up_page.click_sign_up_button()

    def test_carousel(self):
        home_page = HomePage(self._driver)
        home_page.click_about_us_button()
        about_us_page = AboutUsPage(self._driver)
        about_us_page.click_play_video_button()
        about_us_page.click__video_play_control_button()
        about_us_page.hover_over_volume_icon()
        about_us_page.raise_the_volume(20)
        about_us_page.lower_the_volume(15)
        about_us_page.click_full_screen_button()
        about_us_page.click_full_screen_button()

    def test_home_page(self):
        home_page = HomePage(self._driver)
        home_page.click_on_product_by_name("Samsung galaxy s6")

    def test_cart_logged_in_user(self):
        home_page = HomePage(self._driver)
        home_page.click_login_button()
        login_page = LoginPage(self._driver)
        login_page.insert_username(self._config["username"])
        login_page.insert_password(self._config["password"])
        login_page.click_login_button()
        home_page = HomePage(self._driver)

    def test_cart_not_loggen_in(self):
        home_page = HomePage(self._driver)
        home_page.get_product_list()



