import os
import unittest
from infra.UI.browser_wrapper import BrowserWrapper
from infra.json_file_handler import JsonFileHandler
from logic.UI.about_us_page import AboutUsPage
from logic.UI.home_page import HomePage


class TestAboutUsPageUI(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()
        self._config = JsonFileHandler().load_from_file('../../demo_blaze_config.json', __file__)

    def test_about_us_video_play_button(self):
        """
            Test Case 015: Verify that clicking the main play button initiates video play.

        """

        # Pre-conditions
        home_page = HomePage(self._driver)

        # Navigate to the about us page
        home_page.click_about_us_button()
        about_us_page = AboutUsPage(self._driver)

        # Initiate the video player
        about_us_page.click_play_video_button()
        about_us_page.click__video_play_control_button()
        about_us_page.click_full_screen_button()

        # Assert the video state if playing or paused and the screen mode if it is in fullscreen mode
        self.assertTrue(about_us_page.check_state_in_video_is_playing(self._config["paused"]))
        self.assertTrue(about_us_page.check_state_in_video_is_playing(self._config["fullscreen"]))


