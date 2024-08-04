import json


class JsonFileHandler:

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found.")

    @staticmethod
    def save_to_file(filename, data):
        with open(filename, 'w') as filename:
            json.dump(data, filename, indent=4)