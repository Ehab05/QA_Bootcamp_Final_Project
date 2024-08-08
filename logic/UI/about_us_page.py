from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from infra.UI.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AboutUsPage(BasePage):
    CLOSE_BUTTON = "//div[@id='videoModal']//button[@class='btn btn-secondary']"
    X_BUTTON = "//div[@id='videoModal']//button[@class='close']"
    VIDEO_PLAYER = "//div[@id='example-video']"
    MAIN_PLAY_VIDEO_BUTTON = "//button[contains(@title, 'Play Video')]"
    VIDEO_PLAY_CONTROL_BUTTON = "//button[@title='Play'] | //button[@title='Pause']"
    VIDEO_PLAYER_VOLUME_MUTE = "//button[@title='Mute'] | //button[@title='Unmute']"
    VIDEO_PLAYER_VOLUME_BAR = "//div[@class='vjs-volume-control vjs-control vjs-volume-horizontal']/div[@role='slider']"
    FULL_SCREEN_BUTTON = "//button[@title='Fullscreen'] | //button[@title='Non-Fullscreen']"

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._close_button_locator = (By.XPATH, self.CLOSE_BUTTON)
        self._x_button_locator = (By.XPATH, self.X_BUTTON)
        self._video_player_locator = (By.XPATH, self.VIDEO_PLAYER)
        self._main_play_video_button_locator = (By.XPATH, self.MAIN_PLAY_VIDEO_BUTTON)
        self._video_play_control_button_locator = (By.XPATH, self.VIDEO_PLAY_CONTROL_BUTTON)
        self._video_player_volume_mute_locator = (By.XPATH, self.VIDEO_PLAYER_VOLUME_MUTE)
        self._video_player_volume_bar = (By.XPATH, self.VIDEO_PLAYER_VOLUME_BAR)
        self._full_screen_button_locator = (By.XPATH, self.FULL_SCREEN_BUTTON)

    def click_close_button(self):
        close_button = (WebDriverWait(self._driver, 10).until
                        (EC.visibility_of_element_located(self._close_button_locator)))
        close_button.click()

    def click_x_button(self):
        x_button = (WebDriverWait(self._driver, 10).until
                    (EC.visibility_of_element_located(self._x_button_locator)))
        x_button.click()

    def click_play_video_button(self):
        play_video_button = (WebDriverWait(self._driver, 10).until
                             (EC.visibility_of_element_located(self._main_play_video_button_locator)))
        play_video_button.click()

    def click__video_play_control_button(self):
        video_play_control_button = (WebDriverWait(self._driver, 10).until
                                     (EC.presence_of_element_located(self._video_play_control_button_locator)))
        self._driver.execute_script("arguments[0].scrollIntoView();", video_play_control_button)
        video_play_control_button.click()

    def get_video_play_control_button_state(self) -> str:
        """
            Retrieves the current state of the video play control button in the video player.

            This function waits for the video play control button to be present in the DOM and then
            checks its 'title' attribute to determine the current state of the button.
            The state of the button indicates whether the video is currently playing or paused:
            - "Play": The video is currently paused.
            - "Pause": The video is currently playing.

            :return: A string representing the button's state, either "Play" or "Pause".
        """
        video_play_control_button = (WebDriverWait(self._driver, 10).until
                                     (EC.presence_of_element_located(self._video_play_control_button_locator)))
        button_state = video_play_control_button.get_attribute("title")
        return button_state

    def hover_over_volume_icon(self):
        volume_icon = (WebDriverWait(self._driver, 10).until
                       (EC.visibility_of_element_located(self._video_player_volume_mute_locator)))
        action = ActionChains(self._driver)
        action.move_to_element(volume_icon).perform()

    def raise_the_volume(self, desired_volume_percentage):
        volume_bar = (WebDriverWait(self._driver, 10).until
                      (EC.visibility_of_element_located(self._video_player_volume_bar)))
        action = ActionChains(self._driver)
        volume_level_width = volume_bar.find_element(By.CLASS_NAME, "vjs-volume-level").size['width']
        offset_x = (volume_level_width * desired_volume_percentage) / 100
        action.click_and_hold(volume_bar).move_by_offset(offset_x, 0).release().perform()

    def lower_the_volume(self, desired_volume_percentage):
        volume_bar = (WebDriverWait(self._driver, 10).until
                      (EC.visibility_of_element_located(self._video_player_volume_bar)))
        volume_bar_width = self._driver.execute_script("return arguments[0].offsetWidth;", volume_bar)
        current_volume_percentage = int(volume_bar.get_attribute("aria-valuenow"))
        current_offset_x = (volume_bar_width * current_volume_percentage) / 100
        target_offset_x = (volume_bar_width * desired_volume_percentage) / 100
        move_offset_x = target_offset_x - current_offset_x
        action = ActionChains(self._driver)
        action.click_and_hold(volume_bar).move_by_offset(move_offset_x, 0).release().perform()
        return int(volume_bar.get_attribute("aria-valuenow"))

    def click_full_screen_button(self):
        full_screen_button = (WebDriverWait(self._driver, 10).until
                              (EC.visibility_of_element_located(self._full_screen_button_locator)))
        full_screen_button.click()

    def check_state_in_video_is_playing(self, state):
        video_player = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(self._video_player_locator)
        )

        state_to_class = {
            "fullscreen": "vjs-fullscreen",
            "videostarted": "vjs-has-started",
            "playing": "vjs-playing",
            "paused": "vjs-paused"
        }

        expected_class = state_to_class.get(state)

        if expected_class:
            return expected_class in video_player.get_attribute("class")
        else:
            raise ValueError(f"Invalid state: {state}")
