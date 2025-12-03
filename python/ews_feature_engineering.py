# ews_feature_engineering_step1_step2.py
import pandas as pd
import numpy as np
import os

# ============================================================
# CONFIG
# ============================================================
INPUT_CSV = "/Users/shreya/Desktop/DATA/Datasets/CSV_Credit Risk Analysis/loan/loan_cleaned.csv"
OUT_DIR = "validation_outputs"
os.makedirs(OUT_DIR, exist_ok=True)

# ============================================================
# REQUIRED COLUMNS LIST (based on your dataset)
# ============================================================
required_columns = [
    'id','member_id','loan_amnt','funded_amnt','funded_amnt_inv','term','int_rate',
    'installment','grade','sub_grade','emp_title','emp_length','home_ownership',
    'annual_inc','verification_status','issue_d','loan_status','pymnt_plan','url',
    'desc','purpose','title','zip_code','addr_state','dti','delinq_2yrs',
    'earliest_cr_line','inq_last_6mths','mths_since_last_delinq','open_acc','pub_rec',
    'revol_bal','revol_util','total_acc','initial_list_status','out_prncp','out_prncp_inv',
    'total_pymnt','total_pymnt_inv','total_rec_prncp','total_rec_int','total_rec_late_fee',
    'recoveries','collection_recovery_fee','last_pymnt_d','last_pymnt_amnt','next_pymnt_d',
    'last_credit_pull_d','collections_12_mths_ex_med','policy_code','application_type',
    'verification_status_joint','acc_now_delinq','tot_coll_amt','tot_cur_bal','total_rev_hi_lim'
]

print("Loading file:", INPUT_CSV)
df = pd.read_csv(INPUT_CSV, low_memory=False)
print(f"Loaded dataframe with {df.shape[0]:,} rows and {df.shape[1]:,} columns\n")

# ============================================================
# 1. CHECK FOR MISSING REQUIRED COLUMNS
# ============================================================
missing_cols = [c for c in required_columns if c not in df.columns]
if missing_cols:
    print("WARNING: Missing columns:")
    for c in missing_cols:
        print("  -", c)
else:
    print("All expected columns are present.\n")

# ============================================================
# 2. BASIC OVERVIEW
# ============================================================
print("DataFrame info (first 5 columns):")
print(df.iloc[:, :5].head().to_string(index=False))

print("\nData types summary:")
print(df.dtypes.value_counts())

print("\nNon-null counts of important fields:")
key_cols = ['loan_amnt','annual_inc','installment','int_rate','dti','revol_util','loan_status']
for c in key_cols:
    non_null = df[c].notnull().sum()
    print(f"{c}: {non_null:,}/{len(df):,} ({non_null/len(df):.1%})")

# ============================================================
# 3. MISSING VALUES REPORT
# ============================================================
missing_pct = (df.isnull().sum() / len(df) * 100).sort_values(ascending=False)
print("\nTop missing columns:")
print(missing_pct.head(20).to_string())

missing_pct.to_csv(os.path.join(OUT_DIR, "missing_percent.csv"))

# ============================================================
# 4. SAMPLE VALUES FOR SUSPICIOUS COLUMNS
# ============================================================
sample_cols = ['revol_util','int_rate','dti','annual_inc','installment','loan_amnt']
for c in sample_cols:
    print(f"\nSample values for {c}:")
    print(df[c].astype(str).sample(10, random_state=1).tolist())

# ============================================================
# 5. NUMERIC CONVERSION TEST FUNCTION
# ============================================================
def convert_to_numeric(series):
    s = series.astype(str).str.replace("%","", regex=False).str.replace(",","", regex=False).str.strip()
    return pd.to_numeric(s, errors='coerce')

conversion_report = {}
for c in ['revol_util','int_rate','dti','annual_inc','installment','loan_amnt','revol_bal']:
    series = convert_to_numeric(df[c])
    conversion_report[c] = {
        "non_null": df[c].notnull().sum(),
        "converted": series.notnull().sum(),
        "fails": (series.isnull() & df[c].notnull()).sum()
    }

print("\nConversion report:")
for k, v in conversion_report.items():
    print(k, ":", v)

# ============================================================
# 6. VALUE COUNTS CHECK
# ============================================================
for c in ['loan_status','grade','purpose','emp_length','home_ownership','verification_status']:
    print(f"\nValue counts for {c}:")
    print(df[c].value_counts().head(10))

# ============================================================
# 7. FIND PROBLEM ROWS (pandas 2.x fix using concat)
# ============================================================
problem_frames = []

# Convert required numeric fields
ann = convert_to_numeric(df['annual_inc'])
lam = convert_to_numeric(df['loan_amnt'])
dti_num = convert_to_numeric(df['dti'])

if ann.notnull().any():
    problem_frames.append(df[ann <= 0].head(100))

if lam.notnull().any():
    problem_frames.append(df[lam <= 0].head(100))

if dti_num.notnull().any():
    problem_frames.append(df[dti_num > 500].head(100))

if problem_frames:
    problems = pd.concat(problem_frames).drop_duplicates()
    print(f"\nFound {problems.shape[0]} problematic rows. Saved to CSV.")
    problems.to_csv(os.path.join(OUT_DIR, "problem_rows_sample.csv"), index=False)
else:
    print("\nNo problematic rows detected.")

# ============================================================
# 8. SAVE SAMPLE ROWS FOR MANUAL REVIEW
# ============================================================
df.sample(200, random_state=42).to_csv(os.path.join(OUT_DIR, "sample_200_rows.csv"), index=False)
df.head(200).to_csv(os.path.join(OUT_DIR, "first_200_rows.csv"), index=False)

print("\nValidation complete. Output saved in:", OUT_DIR)

# ============================================================
# STEP 2 — START NORMALIZING NUMERIC FIELDS
# ============================================================

print("\nStarting STEP 2: Numeric normalization...")

# Convert numeric-like columns properly
df['loan_amnt_num'] = convert_to_numeric(df['loan_amnt'])
df['annual_inc_num'] = convert_to_numeric(df['annual_inc'])
df['installment_num'] = convert_to_numeric(df['installment'])
df['int_rate_num'] = convert_to_numeric(df['int_rate'])  # kept as percentage form
df['dti_num'] = convert_to_numeric(df['dti'])
df['revol_util_num'] = convert_to_numeric(df['revol_util'])

# Monthly income
df['monthly_income'] = df['annual_inc_num'] / 12

# Installment burden
df['inst_to_income'] = df['installment_num'] / df['monthly_income']
df.loc[df['monthly_income'] <= 0, 'inst_to_income'] = np.nan

print("\nSTEP 2 completed. Fields created:")
print(df[['loan_amnt_num','annual_inc_num','installment_num','int_rate_num','dti_num','revol_util_num','monthly_income','inst_to_income']].head())
# Save the updated dataframe