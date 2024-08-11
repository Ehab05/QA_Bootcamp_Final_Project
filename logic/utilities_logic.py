import json
import os

from faker import Faker

from infra.custom_exception import CustomException
from infra.json_file_handler import JsonFileHandler
from infra.logger import Logger
from logic.credit_card_types import CreditCardType


class UtilitiesLogic:
    def __init__(self):
        # Resolve the path dynamically to avoid issues with the current working directory
        self._config = JsonFileHandler().load_from_file('../demo_blaze_config.json', __file__)
        self._logger = Logger().get_logger()

    def get_url_with_endpoint(self, endpoint):
        """
            Constructs a complete URL by appending the given endpoint to the base URL from the configuration.
        """
        return f"{self._config["api_base_url"]}{endpoint}"

    def get_response_json(self, response):
        # Convert the JSON string to a Python dictionary
        return json.loads(response.text)

    def generate_random_credit_card(self, card_type: CreditCardType) -> dict:
        try:
            # initialize card
            credit_card = {"card_number": "", "card_expiry": "", "card_provider": "", "card_security_code": ""}

            # Create a Faker instance
            fake = Faker()

            # Generate fake credit card information
            credit_card["card_number"] = fake.credit_card_number(card_type=f"{card_type}")
            credit_card["card_expiry"] = fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
            credit_card["card_provider"] = fake.credit_card_provider(card_type=f"{card_type}")
            credit_card["card_security_code"] = fake.credit_card_security_code(card_type=f"{card_type}")
            self._logger.info(f"These are the details for the generated credit card: {credit_card}")

            return credit_card
        except Exception as e:
            raise CustomException(f"Failed to generate credit card: {e}")

