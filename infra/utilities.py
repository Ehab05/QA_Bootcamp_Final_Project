import base64
import random
import string
from faker import Faker


class Utilities:
    def __init__(self):
        pass

    def generate_random_credit_card(self, card_type):
        # initialize card
        credit_card = {"card_number": "", "card_expiry": "", "card_provider": "", "card_security_code": ""}

        # Create a Faker instance
        fake = Faker()

        # Generate fake credit card information
        credit_card["card_number"] = fake.credit_card_number(card_type=f"{card_type}")
        credit_card["card_expiry"] = fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
        credit_card["card_provider"] = fake.credit_card_provider(card_type=f"{card_type}")
        credit_card["card_security_code"] = fake.credit_card_security_code(card_type=f"{card_type}")

        return credit_card

    def generate_random_email(self):
        fake = Faker()
        # Generate a random email address
        fake_email = fake.email()
        # Replace domain with Gmail
        gmail_email = fake_email.split('@')[0] + '@gmail.com'
        return gmail_email

    def generate_random_passwrod(self, password_length) -> str:
        """
            Generating a random password that contains digits and letters with the given length
            :param password_length:
            :return: Password
        """
        letters = string.ascii_letters + string.digits
        return "".join(random.choice(letters) for _ in range(password_length))

    def encode_password(self, password: str) -> str:
        # Encode the password to bytes, then encode the bytes to Base64
        encoded_bytes = base64.b64encode(password.encode('utf-8'))
        # Decode the Base64 bytes to a string
        encoded_str = encoded_bytes.decode('utf-8')
        return encoded_str




