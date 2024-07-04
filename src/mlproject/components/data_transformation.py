from pathlib import Path
from mlproject import logger
from mlproject.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd




class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets (0.75, 0.25) split
        train, test = train_test_split(data)
        train.to_csv(Path(self.config.root_dir) / "train.csv", index=False)
        test.to_csv(Path(self.config.root_dir) / "test.csv", index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(f"{train.shape = }")
        print(f"{test.shape = }")