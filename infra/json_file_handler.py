import json
import os


class JsonFileHandler:

    @staticmethod
    def load_from_file(filename, current_file_path):
        try:
            base_dir = os.path.dirname(os.path.abspath(current_file_path))
            config_file_path = os.path.join(base_dir, filename)
            with open(config_file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found.")

    @staticmethod
    def save_to_file(filename, data):
        with open(filename, 'w') as filename:
            json.dump(data, filename, indent=4)
