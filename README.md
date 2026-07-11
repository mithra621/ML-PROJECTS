# 📊 Student Performance Analysis

An end-to-end **Exploratory Data Analysis (EDA)** project built using **Python** to analyze student performance data. This project explores student scores, visualizes important trends, preprocesses the dataset, and generates meaningful insights using data analysis techniques.
## 🚀 Live Demo

https://studentperformance-analysis.streamlit.app/

---

## 📌 Project Overview

The goal of this project is to analyze the **Students Performance Dataset** and understand the factors affecting students' academic performance.

The project includes:

- Data Loading
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Data Visualization
- Statistical Analysis
- Business Insights

---

## 📂 Project Structure

```
01_student_performance_analysis/
│
├── data/
│   └── StudentsPerformance.csv
│
├── images/
│   ├── math_score_histogram.png
│   ├── reading_score_histogram.png
│   ├── writing_score_histogram.png
│   ├── math_score_boxplot.png
│   ├── reading_score_boxplot.png
│   ├── writing_score_boxplot.png
│   ├── gender_countplot.png
│   ├── race_ethnicity_countplot.png
│   ├── parental_level_of_education_countplot.png
│   ├── lunch_countplot.png
│   ├── test_preparation_course_countplot.png
│   ├── correlation_heatmap.png
│   ├── reading_vs_writing_scatter.png
│   └── pairplot.png
│
├── src/
│   ├── data_loader.py
│   ├── exploration.py
│   ├── preprocessing.py
│   ├── visualization.py
│   ├── analysis.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 📚 Dataset

**Dataset Name:** Students Performance Dataset

The dataset contains information about students including:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

---

# ⚙ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# 🚀 Project Workflow

```
Load Dataset
      ↓
Explore Dataset
      ↓
Data Cleaning
      ↓
Data Visualization
      ↓
Data Preprocessing
      ↓
Data Analysis
      ↓
Generate Insights
```

---

# 📊 Exploratory Data Analysis

The project performs:

- Dataset Shape
- Dataset Information
- Data Types
- Missing Value Analysis
- Duplicate Value Analysis
- Statistical Summary

---

# 📈 Visualizations

The following visualizations are generated automatically:

### 📌 Histograms

- Math Score Distribution
- Reading Score Distribution
- Writing Score Distribution

---

### 📌 Box Plots

- Math Score Box Plot
- Reading Score Box Plot
- Writing Score Box Plot

---

### 📌 Count Plots

- Gender Distribution
- Race/Ethnicity Distribution
- Parental Education Distribution
- Lunch Distribution
- Test Preparation Course Distribution

---

### 📌 Correlation Heatmap

Shows correlation among numerical features.

---

### 📌 Scatter Plot

Reading Score vs Writing Score

---

### 📌 Pair Plot

Relationship among numerical features.

---

# 🧹 Data Preprocessing

The preprocessing module performs:

- Missing Value Check
- Duplicate Removal
- Label Encoding
- Dataset Preparation

---

# 📊 Analysis Performed

The project calculates:

- Average Math Score
- Average Reading Score
- Average Writing Score
- Highest Average Subject
- Gender-wise Performance
- Lunch-wise Performance
- Test Preparation Analysis
- Top Performing Students

---

# 🔍 Key Insights

- The dataset contains **1000 student records**.
- No missing values were found.
- No duplicate records were found.
- Reading scores have the highest average.
- Students who completed the test preparation course generally performed better.
- Students with standard lunch performed better than those with free/reduced lunch.
- Reading and writing scores show a strong positive correlation.

---

# ▶ How to Run

## 1 Clone the repository

```bash
git clone https://github.com/<your-username>/Student-Performance-Analysis.git
```

---

## 2 Navigate to the project

```bash
cd Student-Performance-Analysis
```

---

## 3 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Run the project

```bash
python main.py
```

---

# 📦 Required Libraries

```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

# 📸 Output

Running the project will:

- Load the dataset
- Perform exploratory data analysis
- Generate multiple visualizations
- Save all graphs inside the `images` folder
- Print statistical analysis and insights in the terminal

---

# 🎯 Learning Outcomes

This project helped me understand:

- Data Loading using Pandas
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Data Visualization
- Statistical Analysis
- Label Encoding
- Python Project Structure
- Writing Modular Python Code

---

# 🔮 Future Improvements

- Feature Engineering
- Machine Learning Model
- Prediction System
- Model Evaluation
- Interactive Dashboard using Streamlit
- Model Deployment

---

# 👨‍💻 Author

**Mithra Reddy**

B.Tech – Computer Science & Engineering

GitHub: https://github.com/mithra621

LinkedIn: https://www.linkedin.com/in/mithra-reddy-521a38303

---

## ⭐ If you found this project useful, consider giving it a star!
