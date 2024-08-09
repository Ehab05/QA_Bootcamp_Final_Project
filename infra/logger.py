import logging
import os


class Logger:
    _logger = None

    @classmethod
    def _initialize_logger(cls, log_file='demo_blaze.log', log_dir='logs'):
        if cls._logger is None:
            cls._logger = logging.getLogger()
            cls._logger.propagate = False
            cls._logger.setLevel(logging.INFO)
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # Full path for the log file
            log_dir = os.path.join(project_root, log_dir)
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            log_file_path = os.path.join(log_dir, log_file)

            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler = logging.FileHandler(log_file_path)
            handler.setFormatter(formatter)
            cls._logger.addHandler(handler)

    def get_logger(self):
        self._initialize_logger()  # Ensure logger is initialized
        return self._logger
