import pandas as pd
from read_files import *

def select_columns(df: pd.DataFrame) -> tuple:
    """Input:
    df: DataFrame
        Output:
    numCols: pandas.Index"""
    numCols = df.select_dtypes(include=['int64', 'float64']).columns
    print(type(numCols))
    return numCols
