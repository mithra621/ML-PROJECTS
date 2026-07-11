"""
data_loader.py

This module loads the student performance dataset.
"""

import pandas as pd


def load_data(file_path):
    """
    Load the CSV dataset.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.
    """

    try:
        df = pd.read_csv(file_path)

        print("✅ Dataset Loaded Successfully!")
        print(f"Number of Rows    : {df.shape[0]}")
        print(f"Number of Columns : {df.shape[1]}")

        return df

    except FileNotFoundError:
        print("❌ Dataset file not found.")
        return None

    except Exception as e:
        print(f"Error : {e}")
        return None