from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        """Navigate to a specified URL."""
        self.driver.get(url)

    def get_page_title(self):
        """Get the title of the current page."""
        return self.driver.title

    def get_current_url(self):
        """Get the current URL of the page."""
        return self.driver.current_url

    def take_screenshot(self, file_path):
        """Take a screenshot of the current page."""
        self.driver.save_screenshot(file_path)

    def wait_for_alert_and_accept(self):
        """Wait for an alert to be present and accept it."""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def reload_page(self):
        """Reload the current page."""
        self.driver.refresh()

