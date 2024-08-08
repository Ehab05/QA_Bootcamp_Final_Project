import json
import os
from infra.json_file_handler import JsonFileHandler



class UtilitiesLogic:
    def __init__(self):
        # Resolve the path dynamically to avoid issues with the current working directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(config_file_path)

    def get_url_with_endpoint(self, endpoint):
        """
            Constructs a complete URL by appending the given endpoint to the base URL from the configuration.
        """
        return f"{self._config["api_base_url"]}{endpoint}"

    def get_response_json(self, response):
        # Convert the JSON string to a Python dictionary
        return json.loads(response.text)


