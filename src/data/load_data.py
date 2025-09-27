import pandas as pd
import os
def load_data(file_path:str) -> pd.DataFrame:
    """
    Load data from a CSV file.
    Args:
        path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded DataFrame.
    
    """
    if os.path.exists(file_path) is False:
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    return pd.read_csv(file_path)