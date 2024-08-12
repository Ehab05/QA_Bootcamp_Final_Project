import unittest
from infra.API.api_wrapper import APIWrapper
from infra.utilities import Utilities
from logic.API.API_sign_up_page import APISignUpPage
import pytest


class TestSignUpPageAPI(unittest.TestCase):
    def setUp(self):
        self._request = APIWrapper()

    def test_valid_sign_up(self):
        """
            Test Case 001: Verify successful sign up with valid username and password
        """

        # Initialize API page
        sign_up_api = APISignUpPage(self._request)

        # Send the API call
        response = sign_up_api.sign_up(Utilities().generate_username(8), Utilities().generate_random_password(8))

        # Assert the response
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.ok)

    def test_invalid_sign_up(self):
        """
             Test Case 002:  Verify successful error message for messing password
        """

        # Initialize API page
        sign_up_api = APISignUpPage(self._request)

        # Send the API call
        response = sign_up_api.sign_up(Utilities().generate_username(8), "")

        # Assert the response
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.ok)
