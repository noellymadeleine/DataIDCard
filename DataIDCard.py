from PIL import Image, ImageDraw, ImageFont
import pandas as pd

class DatasetInfo:
    """
    Class to store information about a dataset.

    Attributes:
        shape (tuple): The shape of the dataset as (rows, columns).
        column_names (list): List of column names in the dataset.
        missing_values (Series): Series with the count of missing values per column.
        data_types (Series): Series with the data types of each column.
    """
    def __init__(self, shape, column_names, missing_values, data_types):
        self.shape = shape
        self.column_names = column_names
        self.missing_values = missing_values
        self.data_types = data_types

def collect_dataset_info(data_frame):
    """
    Collects information about a dataset.

    Args:
        data_frame (DataFrame): The input dataset as a pandas DataFrame.

    Returns:
        DatasetInfo: An object containing the collected dataset information.
    """
    # Collect dataset information
    shape = data_frame.shape
    column_names = data_frame.columns.tolist()
    missing_values = data_frame.isnull().sum()
    data_types = data_frame.dtypes

    # Create and return the DatasetInfo object
    return DatasetInfo(shape, column_names, missing_values, data_types)


if __name__ == '__main__':
    df = pd.read_csv("../Oil_pipeline_accidents_analysis/database.csv")
    info = collect_dataset_info(df)

    print("Dataset Shape:", info.shape)
    print("Column Names:", info.column_names)
    print("Missing Values:")
    print(info.missing_values)
    print("Data Types:")
    print(info.data_types)
