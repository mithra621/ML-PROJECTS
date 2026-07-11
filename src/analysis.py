"""
analysis.py

This module performs basic analysis and prints useful insights
from the Student Performance dataset.
"""

import pandas as pd


def analyze_data(df):

    print("\n" + "=" * 70)
    print("DATA ANALYSIS")
    print("=" * 70)

    # ===========================
    # Average Scores
    # ===========================

    print("\nAverage Scores")

    print("-" * 40)

    print(f"Math Score    : {df['math score'].mean():.2f}")
    print(f"Reading Score : {df['reading score'].mean():.2f}")
    print(f"Writing Score : {df['writing score'].mean():.2f}")

    # ===========================
    # Highest Average Subject
    # ===========================

    averages = {
        "Math": df["math score"].mean(),
        "Reading": df["reading score"].mean(),
        "Writing": df["writing score"].mean()
    }

    highest_subject = max(averages, key=averages.get)

    print("\nHighest Average Subject")
    print("-" * 40)
    print(highest_subject)

    # ===========================
    # Gender Analysis
    # ===========================

    print("\nAverage Scores by Gender")
    print("-" * 40)

    print(
        df.groupby("gender")[
            ["math score", "reading score", "writing score"]
        ].mean().round(2)
    )

    # ===========================
    # Lunch Analysis
    # ===========================

    print("\nAverage Scores by Lunch Type")
    print("-" * 40)

    print(
        df.groupby("lunch")[
            ["math score", "reading score", "writing score"]
        ].mean().round(2)
    )

    # ===========================
    # Test Preparation Analysis
    # ===========================

    print("\nAverage Scores by Test Preparation")
    print("-" * 40)

    print(
        df.groupby("test preparation course")[
            ["math score", "reading score", "writing score"]
        ].mean().round(2)
    )

    # ===========================
    # Top 5 Students
    # ===========================

    print("\nTop 5 Students Based on Math Score")
    print("-" * 40)

    top_students = df.sort_values(
        by="math score",
        ascending=False
    ).head(5)

    print(top_students)

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 70)