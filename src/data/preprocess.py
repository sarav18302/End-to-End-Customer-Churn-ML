import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the input DataFrame by handling categorical and numerical columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame to preprocess.
    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    cols_with_no_internet = [
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies'
    ]
    for col in cols_with_no_internet:
        df[col] = df[col].replace('No internet service', 'No')
    
    df.drop(columns=["customerID"], inplace=True)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    return df