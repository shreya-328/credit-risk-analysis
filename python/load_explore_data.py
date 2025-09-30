import pandas as pd

# Load the loan dataset
df = pd.read_csv('/Users/shreya/Desktop/DATA/Datasets/Credit-Risk-Analysis/Credit Risk Analysis/loan/loan.csv')

# Overview of the data
print("Data Info:")
print(df.head())

# Checking for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())  # gives count, min, max, std, mean

print('\nShowing first 5 rows ')
print(df.head())

# Fix mixed type columns by forcing all to string (columns at index 19 and 55)
df.iloc[:, 19] = df.iloc[:, 19].astype(str)
df.iloc[:, 55] = df.iloc[:, 55].astype(str)

# Calculating missing value percentages
missing_percent = (df.isnull().sum() / len(df)) * 100
print("\nMissing Data Percentage per Column:")
print(missing_percent[missing_percent > 0].sort_values(ascending=False))

# Dropping columns with over 70% missing values
threshold = 70
cols_to_drop = missing_percent[missing_percent > threshold].index
df_cleaned = df.drop(columns=cols_to_drop)
print(f"\nDropped columns with >{threshold}% missing values: {list(cols_to_drop)}")

# Checking result after dropping columns
print(f"\nShape after dropping columns: {df_cleaned.shape}")

# Separating numerical and categorical columns
numerical_cols = df_cleaned.select_dtypes(include=['number']).columns
categorical_cols = df_cleaned.select_dtypes(include=['object']).columns

# Impute missing numerical values with median
for col in numerical_cols:
    median_value = df_cleaned[col].median()
    df_cleaned[col].fillna(median_value, inplace=True)

# Impute missing categorical values with mode
for col in categorical_cols:
    mode_value = df_cleaned[col].mode()[0]
    df_cleaned[col].fillna(mode_value, inplace=True)

# Convert categorical columns to 'category' dtype
for col in categorical_cols:
    df_cleaned[col] = df_cleaned[col].astype('category')

# Add 'Unknown' category and fill missing values in 'verification_status_joint'
df_cleaned['verification_status_joint'] = df_cleaned['verification_status_joint'].cat.add_categories(['Unknown'])
df_cleaned['verification_status_joint'] = df_cleaned['verification_status_joint'].fillna('Unknown')

# Strip whitespace and ensure string type for 'verification_status_joint'
df_cleaned['verification_status_joint'] = df_cleaned['verification_status_joint'].astype(str).str.strip()

# Final check for missing values
print(f"\nTotal missing values after cleaning:")
print(df_cleaned.isnull().sum().sum())

# Showing cleaned data info and first few rows
print("\nCleaned Data Info:")
print(df_cleaned.info())

print("\nCleaned Data Sample:")
print(df_cleaned.head())

# Export cleaned data to CSV
df_cleaned.to_csv('loan_cleaned.csv', index=False)


print('-------------------')

print(df_cleaned.columns)
