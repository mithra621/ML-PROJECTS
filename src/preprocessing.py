"""
preprocessing.py

This module preprocesses the dataset for Machine Learning.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):

    print("\n" + "=" * 70)
    print("DATA PREPROCESSING")
    print("=" * 70)

    # -----------------------------
    # Step 1 : Missing Values
    # -----------------------------
    print("\nChecking Missing Values...")

    missing = df.isnull().sum()

    print(missing)

    if missing.sum() == 0:
        print("\n✅ No Missing Values Found.")
    else:
        print("\n⚠ Missing values detected.")
        df = df.dropna()

    # -----------------------------
    # Step 2 : Duplicate Values
    # -----------------------------
    print("\nChecking Duplicate Rows...")

    duplicates = df.duplicated().sum()

    print(f"Duplicate Rows : {duplicates}")

    if duplicates > 0:
        df = df.drop_duplicates()
        print("✅ Duplicate rows removed.")
    else:
        print("✅ No Duplicate Rows Found.")

    # -----------------------------
    # Step 3 : Encode Categorical Columns
    # -----------------------------
    print("\nEncoding Categorical Columns...")

    encoder = LabelEncoder()

    categorical_columns = df.select_dtypes(include="object").columns

    for column in categorical_columns:

        df[column] = encoder.fit_transform(df[column])

        print(f"Encoded : {column}")

    print("\nEncoded Dataset Preview\n")

    print(df.head())

    print("\nPreprocessing Completed Successfully!")

    return df