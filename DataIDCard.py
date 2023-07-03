#!/usr/bin/env python3

"""
This script demonstrates collecting and printing information about a dataset.

It reads a dataset from a CSV file, collects various information about the dataset
such as shape, column names, missing values, and data types, and prints the information
in a nice ASCII format.

The dataset information is stored in a `DatasetInfo` object.

Author: Noelly Madeleine
Date: 03/06/2023
"""

import pandas as pd
import sys

class DatasetInfo:
    """
    Class to store information about a dataset.

    Attributes:
        shape (tuple): The shape of the dataset as (rows, columns).
        column_names (list): List of column names in the dataset.
        missing_values (Series): Series with the count of missing values per column.
        data_types (Series): Series with the data types of each column.
        unique_values (Series): Series with the count of unique values per column.
        value_counts (dict): Dictionary with value counts for each column.
    """
    def __init__(self, shape, column_names, missing_values, data_types, unique_values, value_counts):
        self.shape = shape
        self.column_names = column_names
        self.missing_values = missing_values
        self.data_types = data_types
        self.unique_values = unique_values
        self.value_counts = value_counts

def collect_dataset_info(data_frame):
    """
    Collects information about a dataset.

    Args:
        data_frame (DataFrame): The input dataset as a pandas DataFrame.

    Returns:
        DatasetInfo: An object containing the collected dataset information.
    """
    shape = data_frame.shape
    column_names = data_frame.columns.tolist()
    missing_values = data_frame.isnull().sum()
    data_types = data_frame.dtypes
    unique_values = data_frame.nunique()
    value_counts = {col: data_frame[col].value_counts() for col in column_names}

    return DatasetInfo(shape, column_names, missing_values, data_types, unique_values, value_counts)

def print_dataset_info(info):
    """
    Prints the dataset information.

    Args:
        info (DatasetInfo): The DatasetInfo object containing the dataset information.

    Returns:
        None
    """
    # Print dataset shape
    print("+" + "-" * 40 + "+")
    print("| {:^38} |".format("Dataset Shape"))
    print("+" + "-" * 40 + "+")
    print("| {:^38} |".format("Rows: {:,}".format(info.shape[0])))
    print("| {:^38} |".format("Columns: {:,}".format(info.shape[1])))
    print("+" + "-" * 40 + "+")
    print()

    # Print column names
    print("+" + "-" * 40 + "+")
    print("| {:^38} |".format("Column Names"))
    print("+" + "-" * 40 + "+")
    for column in info.column_names:
        print("| {:<38} |".format(column))
    print("+" + "-" * 40 + "+")
    print()

    # Print missing values
    print("+" + "-" * 40 + "+")
    print("| {:^38} |".format("Missing Values"))
    print("+" + "-" * 40 + "+")
    for column, count in info.missing_values.items():
        print("| {:<38} |".format("{}: {:,}".format(column, count)))
    print("+" + "-" * 40 + "+")
    print()

    # Print data types
    print("+" + "-" * 40 + "+")
    print("| {:^38} |".format("Data Types"))
    print("+" + "-" * 40 + "+")
    for column, dtype in info.data_types.items():
        print("| {:<38} |".format("{}: {}".format(column, dtype)))
    print("+" + "-" * 40 + "+")
    print()


if __name__ == '__main__':
    df = pd.read_csv(sys.argv[1])
    info = collect_dataset_info(df)
    print_dataset_info(info)
