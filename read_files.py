import pandas as pd
import sqlite3 as sql
from contextlib import contextmanager
from pathlib import Path
from uuid import uuid4

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

def readSQL(path:str) -> pd.DataFrame:
    """Input: 
    path: db file path
       Output: 
    Pandas dataframe """
    with sql.connect(path) as engine:
        tableName = (pd.read_sql_query("SELECT * FROM sqlite_master WHERE type = 'table'", engine))['name'][0]
        table = pd.read_sql_query(f"SELECT * FROM {tableName}", engine)
    return table

def SQLconnect(db_bytes):
    fp = Path(str(uuid4()))
    fp.write_bytes(db_bytes.getvalue())
    conn = sql.connect(str(fp))
    return conn

if __name__ == "__main__":
    dataFrameCSV = readCSV("data/housing.csv")

    print(dataFrameCSV)

    dataFrameEXCEL = readExcel("data/housing.xlsx")

    print(dataFrameEXCEL)

    dataFrameSQL = readSQL("data/housing.db")
    
    print(dataFrameSQL)