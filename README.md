# Credit Risk Analysis Project

## 1. Project Overview
This project is an end-to-end Credit Risk Analysis pipeline built using Python and SQL. It identifies patterns of loan default, analyzes borrower risk factors, and provides insights that support data-driven lending decisions. It demonstrates core data analysis skills including data cleaning, exploratory analysis, SQL analytics, and insight generation.

## 2. Business Objective
To analyze borrower demographic, financial, and credit behavior data in order to:
- Identify borrower segments with high default risk
- Understand key drivers of credit risk
- Support lending teams in improving loan approvals, pricing, and portfolio monitoring

## 3. Dataset Information
- Source: Kaggle – Credit Risk Dataset by “ranadeep”
- Contains borrower financial information, demographics, credit behavior, and loan repayment details
- Raw data is available on Kaggle and not stored in this repository

## 4. Project Structure
```
credit-risk-analysis/
├── python/
│   ├── data_cleaning.py
│   └── eda_analysis.py
├── sql/
│   └── SQLQuery_1.sql
└── README.md
```

## 5. Workflow Completed

### Data Cleaning (Python)
- Loaded the raw dataset and reviewed schema
- Removed columns with more than 70% missing data
- Imputed missing numerical values using median
- Imputed categorical missing values using mode or “Unknown”
- Standardized data types and cleaned categorical values
- Exported the cleaned dataset for further analysis

### Exploratory Data Analysis (Python)
- Loan status distribution
- Histograms of annual income, loan amount, interest rate
- Categorical analysis of grade, purpose, employment length
- Outlier detection using boxplots
- Correlation heatmap showing:
  - High correlation between loan amount, funded amount, and installment
  - DTI and revolving utilization as independent risk indicators

### SQL Segmentation and Risk Analysis
- Default rate by loan purpose
- Default rate by grade and sub-grade
- Default rate by employment length and state
- Loan amount bucket analysis
- Default trend over time (month and year)
- Composite risk segmentation using loan amount, DTI, and income
- Feature engineering:
  - DTI risk categories
  - Income brackets
  - Combined risk classifications

## 6. Key Insights and Findings

| Category | Finding | Interpretation |
|----------|---------|----------------|
| Debt-to-Income Ratio | Borrowers with DTI > 25% show higher default rates | Higher repayment pressure increases risk |
| Income Levels | Income < $50,000 is associated with more defaults | Lower repayment capacity |
| Credit Utilization | Revolving utilization > 80% strongly correlates with default | Indicates financial stress |
| Loan Purpose | Small-business, medical, and debt-consolidation loans show higher defaults | Borrowers likely face unstable or emergency expenses |
| Credit Grades | Grades E, F, G show the highest default rates | Lower creditworthiness |
| Combined Risk Factors | High loan amount + high DTI + low income = highest risk segment | Most likely to default |

## 7. Project Summary
This project identifies high-risk borrower groups, explains reasons behind default patterns, and highlights key risk indicators such as DTI, income, credit utilization, loan purpose, and credit grade. Python and SQL were used to build actionable credit risk segmentation that can support underwriting, portfolio monitoring, and credit policy decisions.

## Author
Shreya Nigam
