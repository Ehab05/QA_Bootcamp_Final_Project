from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def navigate_to(self, url):
        """Navigate to a specified URL."""
        self._driver.get(url)

    def get_page_title(self):
        """Get the title of the current page."""
        return self._driver.title

    def get_current_url(self):
        """Get the current URL of the page."""
        return self._driver.current_url

    def take_screenshot(self, file_path):
        """Take a screenshot of the current page."""
        self._driver.save_screenshot(file_path)

    def wait_for_alert_and_accept(self):
        """Wait for an alert to be present and accept it."""
        WebDriverWait(self._driver, 10).until(EC.alert_is_present())
        alert = self._driver.switch_to.alert
        alert.accept()

    def reload_page(self):
        """Reload the current page."""
        self._driver.refresh()

    def add_token_to_cookie(self, token):
        self._driver.add_cookie(token)
        self.reload_page()

