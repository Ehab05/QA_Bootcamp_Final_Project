import logging
import os


class Logger:

    def __init__(self, name, log_file='demo_blaze.log', log_dir='logs'):
        """
        setting up logger class for a project use
        :param name: Name of the logger.
        :param log_file: Name of the log file.
        :param log_dir: Directory where the log file will be created.
        """
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)
        # Ensure the log directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        # Full path for the log file
        log_file_path = os.path.join(log_dir, log_file)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(log_file_path)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def get_logger(self):
        return self._logger
