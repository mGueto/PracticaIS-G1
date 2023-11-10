import pandas as pd
import sqlite3 as sql

def readCSV(path:str) -> pd.DataFrame:
    """Input: 
    path: CSV file path
       Output: 
    Pandas dataframe """
    return pd.read_csv(path)

def readExcel(path:str) -> pd.DataFrame:
    """Input: 
    path: excel file path
       Output: 
    Pandas dataframe """
    return pd.read_excel(path)

def readSQL(tableName:str, path:str) -> pd.DataFrame:
    """Input: 
    tableName: name of the table containing the dataset
    path: db file path
       Output: 
    Pandas dataframe """
    engine = sql.connect(path)
    return pd.read_sql_query(f"SELECT * FROM {tableName}", engine)

if __name__ == "__main__":
    dataFrameCSV = readCSV("data/housing.csv")

    print(dataFrameCSV)

    dataFrameEXCEL = readExcel("data/housing.xlsx")

    print(dataFrameEXCEL)

    dataFrameSQL = readSQL("california_housing_dataset", "data/housing.db")
    
    print(dataFrameSQL)