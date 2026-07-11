import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(
    page_title="Student Performance Analysis",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Student Performance Analysis Dashboard")

st.write(
    """
    This dashboard analyzes the Students Performance dataset
    using Exploratory Data Analysis (EDA).
    """
)

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/StudentsPerformance.csv")

df = load_data()

# Sidebar
st.sidebar.title("Navigation")

option = st.sidebar.selectbox(
    "Select Analysis",
    (
        "Dataset",
        "Statistics",
        "Histograms",
        "Box Plots",
        "Count Plots",
        "Correlation",
        "Scatter Plot"
    )
)

# Dataset
if option == "Dataset":

    st.header("Dataset")

    st.dataframe(df)

# Statistics
elif option == "Statistics":

    st.header("Statistical Summary")

    st.write(df.describe())

# Histograms
elif option == "Histograms":

    st.header("Histogram")

    column = st.selectbox(
        "Choose Score",
        ["math score", "reading score", "writing score"]
    )

    fig, ax = plt.subplots(figsize=(8,5))

    sns.histplot(df[column], kde=True, ax=ax)

    st.pyplot(fig)

# Box Plot
elif option == "Box Plots":

    st.header("Box Plot")

    column = st.selectbox(
        "Choose Score",
        ["math score", "reading score", "writing score"]
    )

    fig, ax = plt.subplots(figsize=(8,5))

    sns.boxplot(x=df[column], ax=ax)

    st.pyplot(fig)

# Count Plot
elif option == "Count Plots":

    st.header("Count Plot")

    column = st.selectbox(
        "Choose Column",
        [
            "gender",
            "race/ethnicity",
            "parental level of education",
            "lunch",
            "test preparation course"
        ]
    )

    fig, ax = plt.subplots(figsize=(10,5))

    sns.countplot(data=df, x=column, ax=ax)

    plt.xticks(rotation=20)

    st.pyplot(fig)

# Heatmap
elif option == "Correlation":

    st.header("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(8,6))

    corr = df.corr(numeric_only=True)

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

# Scatter Plot
elif option == "Scatter Plot":

    st.header("Reading vs Writing")

    fig, ax = plt.subplots(figsize=(8,5))

    sns.scatterplot(
        data=df,
        x="reading score",
        y="writing score",
        hue="gender",
        ax=ax
    )

    st.pyplot(fig)

# Footer
st.markdown("---")
st.write("Created by Mithra Reddy 🚀")