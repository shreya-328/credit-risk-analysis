Credit Risk Analysis Project
1. Project Overview

This project is an end-to-end Credit Risk Analysis pipeline built using Python and SQL. It identifies patterns of loan default, analyzes borrower risk factors, and provides insights that support data-driven lending decisions. It demonstrates core data analyst skills including data cleaning, exploratory analysis, feature engineering, SQL segmentation, and business insight reporting.

2. Business Objective

To analyze borrower demographic, financial, and credit behavior data in order to:

Identify borrower segments with high default risk

Understand key drivers of credit risk

Support lending teams in improving loan approvals, pricing, and portfolio monitoring

3. Dataset Information

Source: Kaggle – Credit Risk Dataset by “ranadeep”

Contains borrower financial information, demographics, credit behavior, and repayment status

Raw data is available on Kaggle and not stored in this repository

4. Project Structure
credit-risk-analysis/
├── python/
│   ├── data_cleaning.py
│   └── eda_analysis.py
├── sql/
│   └── SQLQuery_1.sql
└── README.md

5. Workflow Completed
Data Cleaning (Python)

Loaded the raw dataset and reviewed schema

Removed columns with more than 70% missing data

Imputed missing values using median for numerical columns and mode/“Unknown” for categorical fields

Standardized data types and cleaned categorical values

Exported a cleaned dataset for further analysis

Exploratory Data Analysis (Python)

Analyzed loan status distribution

Examined distributions of loan amount, annual income, interest rate, and installment amounts

Performed categorical analysis for loan grade, loan purpose, and employment length

Detected outliers using boxplots

Generated a correlation heatmap to identify important financial relationships

Confirmed strong correlation among loan amount, funded amount, and installment

Identified DTI and revolving utilization as independent risk indicators

SQL Segmentation and Risk Analysis

Calculated default rates by loan purpose, grade, sub-grade, employment length, state, and loan amount ranges

Analyzed default trends over time (monthly and yearly)

Built composite risk segments such as high loan amount + high DTI + low income

Engineering additional risk flags including:

DTI risk categories

Income brackets

Combined risk classification using DTI and interest rate

6. Key Insights and Findings
Category	Finding	Interpretation
Debt-to-Income Ratio	Borrowers with DTI greater than 25% show significantly higher default rates	Higher repayment pressure leads to greater likelihood of delinquency
Income Levels	Borrowers earning less than $50,000 have higher probability of default	Indicates limited repayment capacity
Credit Utilization	Revolving utilization above 80% strongly correlates with default	High utilization suggests financial stress and overextension
Loan Purpose	Small-business, medical, and debt-consolidation loans show elevated default rates	These purposes align with unstable or emergency financial needs
Credit Grades	Grades E, F, and G have substantially higher default rates	Reflects lower creditworthiness and greater risk
Combined Risk Factors	High loan amount with high DTI and low income forms the highest risk borrower segment	Represents borrowers most likely to default
7. Project Summary

This project identifies high-risk borrower groups, examines financial and behavioral reasons for default, and highlights key indicators such as DTI, income level, credit utilization, loan purpose, and credit grade. The SQL and Python analysis provides actionable risk segmentation and supports improved lending decisions, portfolio monitoring, and credit policy development.

Author

Shreya Nigam
