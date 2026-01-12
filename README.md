# Credit Risk Analysis – Power BI Dashboard

## Project Overview
This project presents an **end-to-end Credit Risk Analysis dashboard built using Power BI**.  
The goal is to analyze borrower risk patterns, identify high-default segments, and provide actionable insights to support **credit policy, lending decisions, and portfolio risk management**.

The project demonstrates complete **Business Intelligence ownership**, including:
- Data transformation and feature engineering using **Power Query**
- Risk metric calculation using **DAX**
- Interactive dashboard design for decision-makers

---

## Business Objective
To help lenders and credit managers:
- Measure overall portfolio default risk
- Identify high-risk borrower segments
- Understand how risk varies by income, loan size, purpose, and time
- Enable data-driven credit approval and risk mitigation decisions

---

## Dataset Information
- **Source:** Kaggle – Credit Risk Dataset (ranadeep)
- **Dataset includes:**
  - Borrower demographics and income
  - Loan attributes (amount, interest rate, grade, purpose)
  - Credit behavior indicators (DTI)
  - Loan outcomes (Fully Paid / Charged Off)

---

## Tools & Technologies Used
- **Power BI Desktop**
- **Power Query** – data cleaning and feature engineering
- **DAX** – KPIs and risk measures
- **SQL** – exploratory analysis and validation (not used in dashboard layer)

---

## Power Query Transformations (Feature Engineering)
All data preparation was performed inside **Power Query**, without using SQL in Power BI:

- Data type standardization and null handling
- Loan Amount Band creation:
  - `<5k`, `5k–10k`, `10k–20k`, `>20k`
- Risk Category classification using DTI and interest rate:
  - High Risk / Medium Risk / Low Risk
- Income Bracket segmentation:
  - Low / Medium / High Income
- Time features derived from loan issue date:
  - Issue Year
  - Issue Month
  - Year-Month

This approach ensures a reusable, scalable, and performance-efficient data model.

---

## Key Metrics (DAX Measures)
The dashboard includes the following business KPIs calculated using **DAX**:

- Total Loans
- Defaulted Loans
- Default Rate
- High-Risk Borrower Percentage
- Average Loan Amount
- Portfolio Risk Distribution

All metrics dynamically respond to slicers and filters.

---

## Dashboard Highlights
The dashboard is structured to answer three core business questions:

### 1. Portfolio Risk Overview
- Overall default rate and portfolio exposure
- Concentration of high-risk borrowers

### 2. Risk Drivers & Segmentation
- Default rate analysis by:
  - Risk Category
  - Loan Amount Band
  - Income Bracket
  - Loan Purpose

### 3. Risk Trends Over Time
- Default rate trends across issue dates
- Identification of risk spikes and behavioral patterns

📄 **Dashboard Export:**  
`Dashboard/Credit Risk Analysis.pdf`

---

## Key Business Insights
- Borrowers with **high DTI and higher interest rates** show significantly higher default rates
- **Low-income segments** consistently exhibit elevated credit risk
- Loans above **20k** carry higher default exposure
- Certain loan purposes (e.g., small business, medical) are riskier
- Default behavior varies over time, highlighting the need for continuous risk monitoring

---

## Repository Structure
