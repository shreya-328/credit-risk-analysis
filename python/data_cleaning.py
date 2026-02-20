import pandas as pd


# ------------------------------------------------------------
# 1. Load Data
# ------------------------------------------------------------

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load raw loan dataset from CSV file.
    """
    return pd.read_csv(file_path, low_memory=False)


# ------------------------------------------------------------
# 2. Drop High Missing Columns
# ------------------------------------------------------------

def drop_high_missing_columns(df: pd.DataFrame, threshold: float = 70.0) -> pd.DataFrame:
    """
    Drop columns with missing percentage above threshold.
    """
    missing_percent = (df.isnull().sum() / len(df)) * 100
    cols_to_drop = missing_percent[missing_percent > threshold].index
    return df.drop(columns=cols_to_drop)


# ------------------------------------------------------------
# 3. Fix Mixed Type Columns (Safe)
# ------------------------------------------------------------

def fix_mixed_types(df: pd.DataFrame, column_indices: list = None) -> pd.DataFrame:
    """
    Force selected columns (by index) to string type safely.
    """
    if column_indices:
        for idx in column_indices:
            if idx < len(df.columns):
                df.iloc[:, idx] = df.iloc[:, idx].astype(str)
    return df


# ------------------------------------------------------------
# 4. Impute Missing Values
# ------------------------------------------------------------

def impute_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Impute numerical columns with median and categorical columns with mode.
    """
    numerical_cols = df.select_dtypes(include=["number"]).columns
    categorical_cols = df.select_dtypes(include=["object"]).columns

    # Numerical → Median
    for col in numerical_cols:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)

    # Categorical → Mode (Safe)
    for col in categorical_cols:
        if not df[col].mode().empty:
            mode_value = df[col].mode()[0]
            df[col] = df[col].fillna(mode_value)

    return df


# ------------------------------------------------------------
# 5. Standardize Specific Columns
# ------------------------------------------------------------

def clean_verification_status_joint(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize verification_status_joint column.
    """
    if "verification_status_joint" in df.columns:
        df["verification_status_joint"] = (
            df["verification_status_joint"]
            .astype(str)
            .str.strip()
            .fillna("Unknown")
        )
    return df


# ------------------------------------------------------------
# 6. Full Cleaning Pipeline
# ------------------------------------------------------------

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full cleaning pipeline combining all cleaning steps.
    """
    df = fix_mixed_types(df, column_indices=[19, 55])
    df = drop_high_missing_columns(df, threshold=70.0)
    df = impute_missing_values(df)
    df = clean_verification_status_joint(df)

    return df


# ------------------------------------------------------------
# 7. Save Cleaned Data
# ------------------------------------------------------------

def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save cleaned dataframe to CSV.
    """
    df.to_csv(output_path, index=False)


# ------------------------------------------------------------
# 8. Run as Script
# ------------------------------------------------------------

if __name__ == "__main__":
    input_path = "data/loan.csv"
    output_path = "data/loan_cleaned.csv"

    raw_df = load_data(input_path)
    cleaned_df = clean_data(raw_df)
    save_cleaned_data(cleaned_df, output_path)

    print("Data cleaning completed successfully.")
