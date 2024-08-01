import requests
from API_test_project_part_b.infra.logger import Logger
from API_test_project_part_b.infra.api.response_wrapper import ResponseWrapper


class APIWrapper:

    def __init__(self):
        self._logger = Logger("fake_rest_API_log").get_logger()
        self._request_response = None
        self._issue = False

    def get_request(self, url, body=None, params=None, headers=None):
        try:

            response = requests.get(url)
            return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=response.json())
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"Error HTTP:{e}")
        except Exception as e:
            self._logger.error(f"Error: {e}")

    def post_request(self, url, body=None, headers=None):
        try:
            response = requests.post(url, json=body, headers=headers)
            return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=response.json())
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"Error HTTP:{e}")
        except Exception as e:
            self._logger.error(f"Error: {e}")

    def put_request(self, url, body=None, headers=None):
        try:
            response = requests.put(url, json=body, headers=headers)
            return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=response.json())
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"Error HTTP:{e}")
        except Exception as e:
            self._logger.error(f"Error: {e}")

    def delete_request(self, url, headers=None):
        try:
            response = requests.delete(url, headers=headers)

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

            return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=data)
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"HTTP error: {e}")
            return None
        except Exception as e:
            self._logger.error(f"Error: {e}")
            return None
