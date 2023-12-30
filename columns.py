import pandas as pd

def selectColumns(df: pd.DataFrame) -> tuple:
    """Input:
    df: DataFrame
        Output:
    numCols: pandas.Index"""
    numCols = df.select_dtypes(include=['int64', 'float64']).columns
    print(type(numCols))
    return numCols
