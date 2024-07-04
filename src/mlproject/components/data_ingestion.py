from pathlib import Path
from mlproject.utils.common import get_size
from mlproject import logger
from urllib import request
import zipfile
from mlproject.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not Path(self.config.local_data_file).exists():
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """Extracts the zip file into the data directory
        
        Args:
            zip_file_path: str

        Returns:
            None
        """
        unzip_path = self.config.unzip_dir
        Path(unzip_path).mkdir(parents=True, exist_ok=True)
        # os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)