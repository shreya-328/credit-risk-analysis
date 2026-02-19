# Credit Risk Analysis & Early Warning System (EWS)

## 1. Project Overview

This project provides an end-to-end Credit Risk Analysis pipeline using Python and SQL. It analyzes borrower financial behavior, identifies high-risk segments, performs default risk segmentation, and lays the groundwork for building an Early Warning System (EWS).

The objective is to support data-driven credit decisioning and proactive portfolio risk monitoring in a banking environment.

---

## 2. Business Objectives

### Phase 1 – Credit Risk Analysis (Completed)
- Identify borrower segments most likely to default
- Analyze financial indicators driving credit risk
- Perform segmentation using SQL-based risk logic
- Generate business insights for credit policy decisions

### Phase 2 – Early Warning System (In Progress)
- Engineer financial stress indicators
- Classify borrowers into Low / Medium / High / Very High early-risk categories
- Detect potential pre-default signals
- Enable proactive borrower monitoring

---

## 3. Dataset Information

- Source: Kaggle – Credit Risk Dataset (ranadeep)
- Data includes:
  - Borrower demographics
  - Loan attributes
  - Income and DTI metrics
  - Credit behavior indicators
  - Repayment outcomes (loan_status)

---

## 4. Project Structure
```
CREDIT-RISK-ANALYSIS/
│
├── Dashboard/
│ ├── Credit Risk Analysis.pbix
│ └── Credit Risk Analysis.pdf
│
├── DFD/
│ ├── Level 0 - DFD.pdf
│ ├── Level_1_DFD.pdf
│ └── Level_2_DFD.pdf
│
├── Figures/
│ ├── count_Each_loan_status.png
│ ├── count_of_loan_grade.png
│ ├── Distribution_of_annual_income.png
│ └── Distribution_of_loan_amount.png
│
├── python/
│ ├── data_cleaning.py
│ ├── eda_analysis.py
│ └── ews_feature_engg.py
│
├── sql/
│ └── SQLQuery_1.sql
│
├── validation_outputs/
│ ├── first_200_rows.csv
│ ├── missing_percent.csv
│ ├── problem_rows_sample.csv
│ └── sample_200_rows.csv
│
├── .gitignore
└── README.md
```

---

## 5. Workflow Summary

### 5.1 Data Cleaning (data_cleaning.py)

- Loaded raw loan dataset
- Identified missing values and calculated missing percentages
- Dropped columns with more than 70% missing data
- Imputed:
  - Numerical columns → Median
  - Categorical columns → Mode
- Converted categorical columns to appropriate data types
- Standardized mixed-type columns
- Exported cleaned dataset as `loan_cleaned.csv`

---

### 5.2 Exploratory Data Analysis (eda_analysis.py)

Performed:

- Loan status distribution analysis
- Loan amount and income distribution analysis
- Loan grade and purpose segmentation
- Employment length distribution
- Default rate calculation by grade
- Outlier detection using boxplots
- Correlation heatmap for key credit features

Visual outputs saved under the Figures directory and used in Power BI dashboard.

---

### 5.3 SQL-Based Risk Segmentation (SQLQuery_1.sql)

Implemented advanced segmentation queries:

- Default rate by:
  - Loan purpose
  - Loan grade and sub-grade
  - Employment length
  - State
  - Time (Year/Month)
- Loan amount bucket segmentation
- Composite segmentation using:
  - High loan amount
  - High DTI
  - Low income
- Risk flag creation:
  - High / Medium / Low Risk categories
  - Income brackets
- Default rate analysis by risk category and income bracket

These queries support portfolio-level credit risk monitoring.

---

### 5.4 Early Warning Feature Engineering (ews_feature_engg.py)

Prepared dataset for Early Warning System development:

- Validated required columns
- Generated missing value reports
- Performed numeric normalization
- Converted percentage-based fields to numeric
- Created financial stress indicators:
  - Monthly income
  - Installment-to-income ratio
- Identified problematic rows
- Exported validation outputs for review

This module forms the foundation for borrower-level early-risk detection.

---

## 6. Key Business Insights

| Risk Driver | Observation | Business Impact |
|-------------|------------|----------------|
| High DTI (>25%) | Higher probability of default | Indicates repayment burden |
| Income < 50K | Increased default frequency | Lower financial stability |
| High Utilization | Strong correlation with default | Credit stress indicator |
| Grades E–G | Highest default rates | Weak credit profile |
| High Loan + High DTI + Low Income | Strongest composite risk | High-risk borrower cluster |

---

## 7. Early Warning System (Next Phase)

The next enhancement of this project focuses on building an Early Warning System (EWS) to:

- Classify borrowers into:
  - Low Risk
  - Medium Risk
  - High Risk
  - Very High Risk
- Detect early financial stress patterns before default
- Quantify risk movement across segments
- Support proactive borrower intervention strategies

This shifts the framework from reactive default analysis to proactive risk monitoring.

---

## 8. Tools & Technologies

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- SQL (Risk segmentation and aggregation)
- Power BI (Dashboard visualization)
- CSV-based validation reporting

---

## 9. Project Summary

This project demonstrates a structured banking analytics workflow:

Data Cleaning → Exploratory Analysis → Risk Segmentation → Feature Engineering → Early Warning Framework

It establishes a strong analytical foundation for developing a proactive credit risk monitoring system.

---

## Author

Shreya Nigam  
Data Analyst – Banking & Risk Analytics
