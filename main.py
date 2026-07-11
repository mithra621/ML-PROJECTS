"""
Student Performance Analysis Project

Author : Mithra Reddy
Description :
End-to-End Exploratory Data Analysis (EDA) Project
"""

# ===========================
# Import Modules
# ===========================

from src.data_loader import load_data
from src.exploration import explore_data
from src.preprocessing import preprocess_data
from src.visualization import (
    create_histograms,
    create_boxplots,
    create_countplots,
    create_heatmap,
    create_scatterplot,
    create_pairplot
)
from src.analysis import analyze_data


# ===========================
# Main Function
# ===========================

def main():

    print("=" * 70)
    print("      STUDENT PERFORMANCE ANALYSIS PROJECT")
    print("=" * 70)

    # ===========================
    # Step 1 : Load Dataset
    # ===========================

    file_path = "data/StudentsPerformance.csv"

    df = load_data(file_path)

    if df is None:
        print("Dataset could not be loaded.")
        return

    # ===========================
    # Step 2 : Preview Dataset
    # ===========================

    print("\n" + "=" * 70)
    print("FIRST FIVE ROWS OF DATASET")
    print("=" * 70)

    print(df.head())

    # ===========================
    # Step 3 : Exploratory Data Analysis
    # ===========================

    explore_data(df)

    # ===========================
    # Step 4 : Visualizations
    # ===========================

    print("\nGenerating Visualizations...\n")

    create_histograms(df)

    create_boxplots(df)

    create_countplots(df)

    create_heatmap(df)

    create_scatterplot(df)

    create_pairplot(df)

    # ===========================
    # Step 5 : Data Preprocessing
    # ===========================

    processed_df = preprocess_data(df)

    # ===========================
    # Step 6 : Data Analysis
    # ===========================

    analyze_data(processed_df)

    # ===========================
    # Project Completed
    # ===========================

    print("\n" + "=" * 70)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print("\nGenerated Files:")

    print("✔ Histograms")
    print("✔ Box Plots")
    print("✔ Count Plots")
    print("✔ Heatmap")
    print("✔ Scatter Plot")
    print("✔ Pair Plot")

    print("\nImages are saved inside the images folder.")

    print("\nThank you for using Student Performance Analysis!")


# ===========================
# Driver Code
# ===========================

if __name__ == "__main__":
    main()