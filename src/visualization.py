"""
visualization.py

This module creates visualizations for the
Student Performance Analysis project.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns

# Graph style
sns.set_style("whitegrid")


# Create images folder
os.makedirs("images", exist_ok=True)


def safe_filename(text):
    """
    Convert a column name into a safe filename.
    """
    return (
        text.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
    )


# =====================================================
# HISTOGRAMS
# =====================================================

def create_histograms(df):

    numerical_columns = [
        "math score",
        "reading score",
        "writing score"
    ]

    print("\nCreating Histograms...\n")

    for column in numerical_columns:

        plt.figure(figsize=(8,5))

        sns.histplot(
            data=df,
            x=column,
            bins=20,
            kde=True,
            color="skyblue"
        )

        plt.title(f"Distribution of {column.title()}")
        plt.xlabel(column.title())
        plt.ylabel("Number of Students")

        filename = f"images/{safe_filename(column)}_histogram.png"

        plt.tight_layout()

        plt.savefig(filename)

        plt.close()

        print(f"✅ Saved: {filename}")


# =====================================================
# BOX PLOTS
# =====================================================

def create_boxplots(df):

    numerical_columns = [
        "math score",
        "reading score",
        "writing score"
    ]

    print("\nCreating Box Plots...\n")

    for column in numerical_columns:

        plt.figure(figsize=(8,5))

        sns.boxplot(
            x=df[column],
            color="orange"
        )

        plt.title(f"Box Plot of {column.title()}")

        filename = f"images/{safe_filename(column)}_boxplot.png"

        plt.tight_layout()

        plt.savefig(filename)

        plt.close()

        print(f"✅ Saved: {filename}")


# =====================================================
# COUNT PLOTS
# =====================================================

def create_countplots(df):

    categorical_columns = [
        "gender",
        "race/ethnicity",
        "parental level of education",
        "lunch",
        "test preparation course"
    ]

    print("\nCreating Count Plots...\n")

    for column in categorical_columns:

        plt.figure(figsize=(10,5))

        sns.countplot(
            data=df,
            x=column,
            palette="viridis"
        )

        plt.xticks(rotation=20)

        plt.title(f"Count Plot of {column.title()}")

        filename = f"images/{safe_filename(column)}_countplot.png"

        plt.tight_layout()

        plt.savefig(filename)

        plt.close()

        print(f"✅ Saved: {filename}")


# =====================================================
# HEATMAP
# =====================================================

def create_heatmap(df):

    print("\nCreating Heatmap...\n")

    plt.figure(figsize=(8,6))

    correlation = df.corr(numeric_only=True)

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        linewidths=1
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    filename = "images/correlation_heatmap.png"

    plt.savefig(filename)

    plt.close()

    print(f"✅ Saved: {filename}")


# =====================================================
# SCATTER PLOT
# =====================================================

def create_scatterplot(df):

    print("\nCreating Scatter Plot...\n")

    plt.figure(figsize=(8,6))

    sns.scatterplot(
        data=df,
        x="reading score",
        y="writing score",
        hue="gender"
    )

    plt.title("Reading Score vs Writing Score")

    plt.tight_layout()

    filename = "images/reading_vs_writing_scatter.png"

    plt.savefig(filename)

    plt.close()

    print(f"✅ Saved: {filename}")


# =====================================================
# PAIR PLOT
# =====================================================

def create_pairplot(df):

    print("\nCreating Pair Plot...\n")

    pair = sns.pairplot(
        df[
            [
                "math score",
                "reading score",
                "writing score"
            ]
        ]
    )

    filename = "images/pairplot.png"

    pair.savefig(filename)

    plt.close()

    print(f"✅ Saved: {filename}")