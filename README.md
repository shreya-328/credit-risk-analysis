# Credit Risk Analysis Project

## Project Overview
This project is a complete end-to-end data analysis pipeline for Credit Risk Assessment, it is built to demonstrate best practices for a data analyst portfolio. It includes Data Cleaning, Exploratory Data Analysis(EDA) using Python, and is structured for further SQL and Power BI Dashboard Development.

## Business Objective:
Identify patters of default risk in loan applicants and inform risk-driven lending decisions.

## Dataset Information
- Source: [Kaggle Credit Risk Dataset by ranadeep](https://www.kaggle.com/datasets/ranadeep/credit-risk-dataset)
- Dataset includes borrower financial, demographic, and loan repayment information.
- Raw dataset files are stored in the `data/raw/` folder (not included in this repository; please download from Kaggle).

## Project Structure
```credit-risk-analysis/
├── python/
│   ├── data_cleaning.py
│   └── eda_analysis.py
├── sql/
│   └── SQLQuery_1.sql
└── README.md
```

## Workflow & Steps Completed

1. Data Cleaning (Python)
   - Loaded raw dataset, reviewed schema/types
   - Dropped columns with >70% missing data
   - Imputed missing values:
       -**Numerical:** median
       -**Categorical:** mode or 'Unknown'
   - Standardized data types and cleaned text columns
   - Exported Cleaned Data for further analysis

2. Exploratory Data Analysis (EDA)
    - Target Variable Analysis : Loan Status Distribution (Counts & Plots)
    - Numerical Distributions: Loan Amount, Income, Interest Rate, Installments (Histograms, Boxplots)
    - Categorical Features : Grade, Purpose, Employment Length (Barplots, Value Counts)
    - Default Rate Analysis: By Grafe, Purpose, and Segment
    - Correlation Heatmap: Detected redundant vs unique features for modeling
        - High Correlation among loan_amnt, funded_amnt, installment-one retained for analysis
        - DTI and Revolving Utilization are independent risk factors
        - Interest Rate and Annual Income show limited Correlation
    - Summary of Insights : informs all next SQL and Dashboard Work
          
3. Prepared for Next Phase
    - All Cleaning and EDA completed
    - Ready to move to Advancced SQL and Power BI
  
## Key Visuals and Outputs
  - Loan Status Bar Chart
  - Histograms for Loan Amount, Income, Rate
  - BoxPlots for outlier analysis
  - Category bar charts for Grade, Purpose
  - Correlation Heatmap for major features
  - Default rates by Key Business Segments

## Next Steps
Business Problem & Approach (Next Phase) 

Business Problem 

Lending institutions face high financial risk when borrowers default on loans. The goal is to use borrower demographic, financial, and credit behavior data to predict the likelihood of loan default, enabling banks to make more informed lending decisions, optimize risk exposure, and improve portfolio quality. 

Approach for the Upcoming Stages 

To solve this, the project will extend beyond data cleaning and EDA into advanced analytic steps used in real credit-risk teams: 

Feature Engineering 

- Create borrower risk indicators such as DTI buckets, interest-rate bands, credit utilization flags, income tiers, installment-to-income ratio, and combined risk categories. 

- Enhance interpretability by building business-friendly categorical variables. 

Credit Risk Modeling (Supervised Machine Learning) 

- Convert loan_status into a binary default flag. 

- Train baseline and advanced models (Logistic Regression, Random Forest, XGBoost). 

- Evaluate models with industry metrics: ROC-AUC, Precision/Recall, Confusion Matrix. 

- Generate Probability of Default (PD) for each borrower. 

Risk Scorecard Development 

- Translate PD predictions into a scorecard similar to those used by credit bureaus. 

- Create risk buckets (Low, Medium, High, Very High Risk) for business decisions. 

Business Insights Development 

- Identify segments with the highest expected loss. 

R- ecommend changes in credit policy, pricing strategy, and approval rules. 

- Provide actionable insights for risk managers and underwriters. 

Dashboard & Reporting (Power BI / Tableau) 

- Build a comprehensive Credit Risk Dashboard containing: 

- Portfolio overview 

- Default trends 

- Risk segmentation 

- Top risky borrower profiles 

- State-wise and purpose-wise performance 

Final output will serve as a presentation-ready analytical story for portfolio monitoring. 

 ────────────────────────────────────────────────────────────────────
                    CREDIT RISK ANALYSIS — SUMMARY
────────────────────────────────────────────────────────────────────

BUSINESS GOAL:
  ✔ Identify high-default borrower segments
  ✔ Understand drivers of credit risk
  ✔ Help lenders make better approval, pricing & monitoring decisions

APPROACH:
  1. Data Cleaning (Python)
  2. EDA (Python)
  3. Risk Segmentation (SQL)
  4. Feature Engineering (SQL)
  5. Business Insights & Recommendations

KEY QUESTIONS ANSWERED:
  ✔ Who defaults?
  ✔ Why do they default?
  ✔ Which borrower groups are most risky?
  ✔ Which financial attributes drive risk?
  ✔ Which segments need stricter lending rules?

HOW IT WAS SOLVED:
  → Python: cleaning, distributions, outliers, correlations
  → SQL: segmentation, default rates, composite risk flags
  → Insights: DTI, income, purpose, sub-grade, utilization are strongest predictors

BUSINESS OUTCOME:
  → Clear understanding of borrower risk
  → Action-ready risk categories
  → Data-driven lending decisions
────────────────────────────────────────────────────────────────────


## Author
Shreya Nigam
   
