import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def get_unique_values(df:pd.DataFrame):
    for col in df.columns:
        print(f"{col}: {df[col].unique()}")

def dataset_summary(df:pd.DataFrame):
    print("*** Dataset Summary ***")
    print("Dataframe Shape:", df.shape)
    print("\nDataframe Info:")
    print(df.info())
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nUnique Values per Column:")
    get_unique_values(df)
    print("\nStatistical Summary:\n", df.describe(include='all'))
    print("***** End of Summary *****")

def handle_numerical_cols(df:pd.DataFrame) -> pd.DataFrame:
    """
    Normalize all numerical columns to range [0, 1]
    """
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns.difference(['Churn'])
    scaler = MinMaxScaler(feature_range=(0, 1))
    df[num_cols] = scaler.fit_transform(df[num_cols])
    return df

def handle_categorical_cols(df:pd.DataFrame) -> pd.DataFrame:
    
    """
    Handle categorical columns by encoding them appropriately.
    """

    binary_cols = [col for col in df.columns if df[col].nunique() == 2]
    categorical_cols = df.select_dtypes(include=['object']).columns.difference(binary_cols)
    print("Categorical columns to be one-hot encoded:", categorical_cols)
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    binary_cols = [col for col in df.columns if df[col].nunique() == 2 and col != 'Churn']
    print("Binary columns:", binary_cols)

    for col in binary_cols:
        df[col] = df[col].map({df[col].unique()[0]: 0, df[col].unique()[1]: 1})
    df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform feature engineering on the input DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame to engineer features on.
    Returns:
        pd.DataFrame: DataFrame with engineered features.
    """
    dataset_summary(df)
    print("First 5 rows of the dataset:")
    print(df.head())
    df = handle_categorical_cols(df)
    df = handle_numerical_cols(df)
    
    
    return df