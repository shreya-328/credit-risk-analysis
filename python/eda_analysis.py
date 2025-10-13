import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('/Users/shreya/Desktop/DATA/Datasets/CSV_Credit Risk Analysis/loan/loan_cleaned.csv')

#Quick overview of the data
print(df.shape) #rows and columns
print(df.info()) #data types and non-null counts
print(df.head()) #first few rows

# # Target Variable Analysis
print(df['loan_status'].value_counts())

# # Visualize Loan Status
sns.countplot(data=df,x='loan_status')
plt.title('Count of Each Loan Status')
plt.xticks(rotation=70)
plt.show()

# # Distribution of Numerical Features
sns.histplot(data=df['loan_amnt'], bins=30, kde=True)
plt.title('Distribution of Loan Amount')
plt.show()

sns.histplot(data=df['annual_inc'], bins=30, kde=True)
plt.title('Distribution of Annual Income')
plt.show()

# Analyze Important Categorical Features ex loan grade, purpose, employment length
print(df['grade'].value_counts())
sns.countplot(data=df, x='grade', order=sorted(df['grade'].unique()))
plt.title('Count of Loan Grades')
plt.show()

print(df['purpose'].value_counts())
sns.countplot(data=df, x='purpose')
plt.title('Count of Loan Purposes')
plt.xticks(rotation=70)
plt.show()

# Outlier Detection with Boxplots
sns.boxplot(x=df['annual_inc'])
plt.title('Annual Income Outliers')
plt.show()

#Default rates by Segment
default_rates = df.groupby('grade')['loan_status'].apply(lambda x: (x == 'Charged Off').mean())
print(default_rates)
default_rates.plot(kind='bar', title='Default Rates by Loan Grade')
plt.ylabel('Default Rate')
plt.show()

# Correlation Heatmap

selected_cols = [
    "loan_amnt", "funded_amnt", "annual_inc", "int_rate",
    "installment", "dti", "revol_bal", "revol_util", "total_acc"
]
corr = df[selected_cols].corr()

plt.figure(figsize=(10, 7))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Correlation of Key Credit Risk Features")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()