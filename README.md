# Credit Risk Analysis Project

## 1. Project Overview
This project provides an end-to-end Credit Risk Analysis pipeline using Python and SQL. It identifies borrower segments with high default risk, analyzes financial drivers of borrower behavior, and delivers insights that support improved lending decisions, pricing strategy, and portfolio risk management.

## 2. Business Objective
To analyze borrower demographic, financial, and credit behavior data in order to:
- Identify borrower groups most likely to default
- Understand the financial indicators that drive credit risk
- Support data-driven lending and credit policy decisions

## 3. Dataset Information
- Source: Kaggle – Credit Risk Dataset by “ranadeep”
- Contains borrower demographics, income, loan attributes, credit behavior, and repayment outcomes

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

## 5. Workflow Summary

### Data Cleaning (Python)
- Removed columns with excessive missing values
- Imputed numerical and categorical missing values
- Cleaned and standardized dataset for analysis

### Exploratory Data Analysis (Python)
- Examined loan status distribution
- Analyzed income, loan amount, interest rate, and installment patterns
- Assessed grade, purpose, and employment length distributions
- Identified outliers and analyzed feature correlations

### SQL-Based Risk Segmentation
- Default rate analysis by loan purpose, grade, sub-grade, employment length, and geography
- Loan amount bucket segmentation
- Time-based default behavior
- Composite segmentation using DTI, income, and loan amount
- Feature engineering to create risk-based borrower categories

## 5.1 Data Flow Diagram (DFD Level 0)

The following diagram shows the high-level flow of data from the raw applicant dataset into the
Credit Risk Analysis System, and how cleaned/segmented risk outputs are produced for stakeholders.

📄 **View PDF:**  
[DFD Level 0 – Credit Risk Analysis System](./DFD/Level%200%20-%20DFD.pdf)

## 6. Key Insights

| Factor | Finding | Interpretation |
|--------|---------|----------------|
| Debt-to-Income Ratio | DTI > 25% correlates with higher defaults | Indicates repayment burden and limited cash flow |
| Income Level | Income < $50,000 defaults more often | Lower financial stability |
| Credit Utilization | Utilization > 80% strongly predicts default | Signs of borrower financial stress |
| Loan Purpose | Small-business and medical loans show higher risk | Unstable or emergency financial needs |
| Credit Grades | Grades E, F, G have the highest default rates | Indicates weaker creditworthiness |
| Combined Factors | High loan amount + high DTI + low income | Strongest indicator of default likelihood |

## 7. Upcoming Business Problem: Early Warning System (EWS)
The next phase of this project focuses on developing an Early Warning System to detect pre-default risk using borrower financial behavior indicators. The goal is to classify borrowers into Low, Medium, High, and Very High Early-Risk categories.

### Planned Objectives
- Engineer financial stress indicators such as DTI buckets, utilization flags, installment burden, and income tiers
- Build composite early-risk categories using SQL and Python
- Quantify default likelihood within each early-risk segment
- Provide actionable recommendations for credit policy and proactive borrower intervention

This enhancement supports proactive risk management and strengthens the overall credit decisioning framework.

## 8. Project Summary
This project delivers a complete workflow from data cleaning to risk segmentation and uncovers meaningful insights into borrower behavior. The upcoming Early Warning System will extend the analysis by enabling proactive detection of repayment stress and further improving portfolio risk management.

## Author
Shreya Nigam
