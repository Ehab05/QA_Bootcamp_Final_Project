import json


class JsonFileHandler:

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found.")
