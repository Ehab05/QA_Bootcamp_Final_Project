import os


class UtilsLogic:
    def __init__(self):
        # Resolve the path dynamically to avoid issues with the current working directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../../fake_rest_config.json')
        self._config = ConfigProvider().load_from_file(config_file_path)

    def get_url_with_endpoint(self, endpoint):
        """
            Constructs a complete URL by appending the given endpoint to the base URL from the configuration.
        """
        return f"{self._config["base_url"]}{endpoint}"
