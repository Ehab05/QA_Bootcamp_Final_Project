import base64
import random
import string
import time
from faker import Faker
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.custom_exception import CustomException
from infra.logger import Logger


class Utilities:
    def __init__(self):
        self._logger = Logger().get_logger()

    def generate_username(self, username_length: int) -> str:
        """
        Generating a random username that contains letters with the given length
        :param username_length:
        :return: Username
        """
        letters = string.ascii_letters
        return "".join(random.choice(letters) for _ in range(username_length))



    def generate_random_email(self, email_host) -> str:
        """
        Generates a random fake email with given email host
        :param email_host: Enter the email host in this structure: @email_host.com
        :return: fakename@email_host.com
        """
        fake = Faker()
        # Generate a random email address
        fake_email = fake.email()
        # Replace domain with host email
        email = fake_email.split('@')[0] + f"{email_host}"
        return email

    def generate_random_password(self, password_length) -> str:
        """
            Generating a random password that contains digits and letters with the given length
            :param password_length:
            :return: Password
        """
        letters = string.ascii_letters + string.digits
        return "".join(random.choice(letters) for _ in range(password_length))

    def encode_password_by_base64(self, password: str) -> str:
        # Encode the password to bytes, then encode the bytes to Base64
        encoded_bytes = base64.b64encode(password.encode('utf-8'))
        # Decode the Base64 bytes to a string
        encoded_str = encoded_bytes.decode('utf-8')
        return encoded_str

    def scramble_password(self, password):
        """
            This function get a password and rearrange the letters in a random way
            :param password:
            :return: Scrambled password
        """
        return "".join(random.sample(password, len(password)))

    def generate_paragraph(self, min_sentences: int, max_sentences: int):
        """
           Generates a random paragraph composed of a specified range of sentences.

           Parameters:
           ----------
           min_sentences : int
               The minimum number of sentences to include in the paragraph.
           max_sentences : int
               The maximum number of sentences to include in the paragraph.

           Returns:
           -------
           str
               A string representing a paragraph composed of randomly generated sentences.
        """
        fake = Faker()
        # Randomly determine the number of sentences in the paragraph
        num_sentences = random.randint(min_sentences, max_sentences)

        # Generate the specified number of sentences
        sentences = [fake.sentence() for _ in range(num_sentences)]

        # Join sentences to form a paragraph
        paragraph = ' '.join(sentences)

        return paragraph

    def retry_waiting_for_element_to_click(self, retries, driver, path):
        """
            Repeatedly attempts to locate and click an element on a webpage.

            This function will try to find and click an element specified by the given XPath. If the element is not found or not clickable,
            it will retry the operation a specified number of times before raising an exception.

            Args:
                retries (int): The number of times to retry locating and clicking the element.
                driver (WebDriver): The Selenium WebDriver instance to interact with the browser.
                path (str): The XPath locator of the element to be clicked.

            Raises:
                CustomException: If the element cannot be found or clicked after the specified number of retries.

            Exceptions:
                StaleElementReferenceException: Raised if the referenced element is no longer in the DOM.
                TimeoutException: Raised if the element is not found within the specified time.

            Returns:
                None
            """
        while retries > 0:
            try:
                time.sleep(1)
                element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, path))
                )
                # Wait for the product link to be clickable
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, path))
                )
                element.click()
                return
            except (StaleElementReferenceException, TimeoutException):
                retries -= 1
                if retries == 0:
                    raise CustomException(f"Failed to find the element")

    @staticmethod
    def wait_for_action(action, sleep_time, retries):
        """
        This function effectively waits for an action to succeed, retrying every `sleep_time` seconds for `retries` times.

        :param action: A callable that performs the desired action and returns a result.
        :param sleep_time: Time in seconds to wait between retries.
        :param retries: Number of times to retry the action if it fails.
        :return: The result of the action if successful, otherwise False.
        """
        result = None
        while retries > 0:
            try:
                result = action()
                if result:
                    return result
            except Exception as e:
                print(f"Action failed with exception: {e}. Retrying...")
            time.sleep(sleep_time)
            retries -= 1
        return False
