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
│   └── eda_analysis.ipynb
├── sql/
│   └── analysis_queries.sql
└── README.md
```

## Workflow & Steps Completed

1. Data Cleaning (Python)
   - Loaded raw dataset, reviewed schema/types
   - Dropped columns with >70% missing data
   - Imputed missing values:
       -**Numerical:**median
       -**Categorical:**mode or 'Unknown'
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
  - Targeted SQL queries for deeper Business Insights
  - Power BI/LookerStudio/Tableau Dashboard using key EDA findings for clear, actionable Stortelling

## Author
Shreya Nigam
   





















