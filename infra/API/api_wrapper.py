import requests

from infra.API.response_wrapper import ResponseWrapper
from infra.logger import Logger


class APIWrapper:

    def __init__(self):
        self._logger = Logger("fake_rest_API_log").get_logger()
        self.auth_token = None
        self._session = requests.Session()

    def get_request(self, url, body=None, params=None, headers=None):
        try:

            response = self._session.get(url)
            return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=response.json(), text=response.text, cookies=response.cookies)
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"Error HTTP:{e}")
        except Exception as e:
            self._logger.error(f"Error: {e}")

    def post_request(self, url, body=None, headers=None):
        try:
            response = self._session.post(url, json=body, headers=headers)
            return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=response.json(), text=response.text, cookies=response.cookies)
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"Error HTTP:{e}")
        except Exception as e:
            self._logger.error(f"Error: {e}")

    def put_request(self, url, body=None, headers=None):
        try:
            response = self._session.put(url, json=body, headers=headers)
            return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=response.json(), text=response.text, cookies=response.cookies)
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"Error HTTP:{e}")
        except Exception as e:
            self._logger.error(f"Error: {e}")

    def delete_request(self, url, headers=None):
        try:
            response = self._session.delete(url, headers=headers)

            # Check if the response body is empty
            if response.content:
                try:
                    data = response.json()
                except ValueError as e:
                    # Log JSON decoding error if response body is not valid JSON
                    self._logger.error(f"JSON decoding error: {e}")
                    self._logger.error(f"Response content: {response.text}")
                    data = None
            else:
                # Response body is empty, which is expected
                data = None

            return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=data, text=response.text, cookies=response.cookies)
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"HTTP error: {e}")
            return None
        except Exception as e:
            self._logger.error(f"Error: {e}")
            return None

    def set_auth_token(self, token):
        """Sets the authentication token for API requests."""
        self._session.headers.update({"Authorization": f"Bearer {token}"})
