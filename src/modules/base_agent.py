import os
import logging
import csv
from abc import ABC, abstractmethod


class BaseAgent(ABC):
    def __init__(self, project_folder: str):
        self.logger = None
        self.project_folder = os.path.abspath(project_folder)
        os.makedirs(self.project_folder, exist_ok=True)
        self.setup_logging()

    def setup_logging(self):
        """Set up logging for the module."""
        log_file = os.path.join(self.project_folder, "../logs/app.log")
        logging.basicConfig(level=logging.INFO, filename=log_file,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(self.__class__.__name__)

    def write_to_csv(self, filename: str, data: list):
        """Write list data to a CSV file."""
        file_path = os.path.join(self.project_folder, filename)
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data[0].keys())  # Write headers
            for row in data:
                writer.writerow(row.values())
        self.logger.info(f"Data written to {file_path}")

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Each subclass must implement this method."""
        pass
