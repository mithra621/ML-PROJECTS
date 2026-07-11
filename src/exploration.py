"""
exploration.py

This module explores the dataset.
"""

def explore_data(df):

    print("\n" + "="*60)
    print("DATASET INFORMATION")
    print("="*60)

    # Shape
    print("\nShape of Dataset:")
    print(df.shape)

    # Columns
    print("\nColumn Names:")
    print(df.columns)

    # Data Types
    print("\nData Types:")
    print(df.dtypes)

    # Information
    print("\nDataset Information:")
    df.info()

    # Missing Values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Duplicate Values
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    # Statistics
    print("\nStatistical Summary:")
    print(df.describe())