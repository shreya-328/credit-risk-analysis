import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading data

def load_data(file_path : str) -> pd.DataFrame:
    return pd.read_csv(file_path,low_memory=False)

# Basic summary
def summarize_data(df:pd.DataFrame)-> dict:
    """
    returns basic data summary
    """
    summary = {
        "shape":df.shape,
        "columns": df.columns.tolist(),
        "loan_status_distribution":df["loan_status"].value_counts().to_dict()
    }
    return summary

# default rate analysis ie DR by grade and purpose and correl matrix

def calculate_default_rate(df:pd.DataFrame,group_by_column:str)-> pd.DataFrame:
    """
    «calculates default rate grouped by a given column.
    """
    grouped = df.groupby(group_by_column)["loan_status"].apply(
        lambda x:(x=="Charged Off").mean()
    ).reset_index(name="default_rate")
    return grouped

#Correlation Analysis
def calculate_correl(df: pd.DataFrame, selected_columns:list)-> pd.DataFrame:
    """
    returns correl matrix for selected numeric columns
    """
    return df[selected_columns].corr()

#STEP 3 Visualtization Layer (Controlled - i can see the visuals whenever i want)
#VIZ function

def plot_loan_status_distribution(df:pd.DataFrame):
    plt.figure(figsize=(8,5))
    sns.countplot(data=df,x="loan_status")
    plt.title("Loan Status Distribution")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_default_rate(df:pd.DataFrame, group_by_column:str):
    default_rates = calculate_default_rate(df, group_by_column)

    plt.figure(figsize=(8, 5))
    sns.barplot(data=default_rates, x=group_by_column, y="default_rate")
    plt.title(f"Default Rate by {group_by_column}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#Numerical Distribution plot
def plot_numeric_distribution(df: pd.DataFrame, column: str):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], bins=30, kde=True)
    plt.title(f"Distribution of {column}")
    plt.tight_layout()
    plt.show()

# Categorical Count Plot
def plot_categorical_count(df: pd.DataFrame, column: str):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x=column)
    plt.title(f"Count of {column}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Boxplot (Outlier View)
def plot_boxplot(df: pd.DataFrame, column: str):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.tight_layout()
    plt.show()

# Correlation Heatmap
def plot_correlation_heatmap(df: pd.DataFrame, selected_columns: list):
    corr = calculate_correl(df, selected_columns)

    plt.figure(figsize=(10, 7))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
    plt.title("Correlation Heatmap")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()


# 6. Run EDA Manually (Optional)

import os

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "data", "loan_cleaned.csv")

    df = load_data(file_path)

    summary = summarize_data(df)
    print(summary)

    # ---- Visualizations ----
    plot_loan_status_distribution(df)

    plot_numeric_distribution(df, "loan_amnt")
    plot_numeric_distribution(df, "annual_inc")

    plot_categorical_count(df, "grade")
    plot_categorical_count(df, "purpose")

    plot_boxplot(df, "annual_inc")

    plot_default_rate(df, "grade")

    selected_cols = [
        "loan_amnt", "funded_amnt", "annual_inc",
        "int_rate", "installment", "dti",
        "revol_bal", "revol_util", "total_acc"
    ]

    plot_correlation_heatmap(df, selected_cols)

















# df= pd.read_csv('/Users/shreya/Desktop/DATA/Datasets/CSV_Credit Risk Analysis/loan/loan_cleaned.csv')

# #Quick overview of the data
# print(df.shape) #rows and columns
# print(df.info()) #data types and non-null counts
# print(df.head()) #first few rows

# # # Target Variable Analysis
# print(df['loan_status'].value_counts())

# # # Visualize Loan Status
# sns.countplot(data=df,x='loan_status')
# plt.title('Count of Each Loan Status')
# plt.xticks(rotation=70)
# plt.show()

# # # Distribution of Numerical Features
# sns.histplot(data=df['loan_amnt'], bins=30, kde=True)
# plt.title('Distribution of Loan Amount')
# plt.show()

# sns.histplot(data=df['annual_inc'], bins=30, kde=True)
# plt.title('Distribution of Annual Income')
# plt.show()

# # Analyze Important Categorical Features ex loan grade, purpose, employment length
# print(df['grade'].value_counts())
# sns.countplot(data=df, x='grade', order=sorted(df['grade'].unique()))
# plt.title('Count of Loan Grades')
# plt.show()

# print(df['purpose'].value_counts())
# sns.countplot(data=df, x='purpose')
# plt.title('Count of Loan Purposes')
# plt.xticks(rotation=70)
# plt.show()

# # Outlier Detection with Boxplots
# sns.boxplot(x=df['annual_inc'])
# plt.title('Annual Income Outliers')
# plt.show()

# #Default rates by Segment
# default_rates = df.groupby('grade')['loan_status'].apply(lambda x: (x == 'Charged Off').mean())
# print(default_rates)
# default_rates.plot(kind='bar', title='Default Rates by Loan Grade')
# plt.ylabel('Default Rate')
# plt.show()

# # Correlation Heatmap

# selected_cols = [
#     "loan_amnt", "funded_amnt", "annual_inc", "int_rate",
#     "installment", "dti", "revol_bal", "revol_util", "total_acc"
# ]
# corr = df[selected_cols].corr()

# plt.figure(figsize=(10, 7))
# sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
# plt.title("Correlation of Key Credit Risk Features")
# plt.xticks(rotation=45)
# plt.yticks(rotation=0)
# plt.tight_layout()
# plt.show()