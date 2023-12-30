import sqlite3 as sql
from contextlib import contextmanager
from pathlib import Path
from uuid import uuid4
import pandas as pd

#Las funciones internas son privadas ya que solo se usan dentro de esa función
def ReadFiles(uploaded_file):

    if uploaded_file.name.endswith('.csv'):
        data = _readCSV(uploaded_file) 
    elif uploaded_file.name.endswith('.xlsx'):
        data = _readExcel(uploaded_file)
    else:
        uploaded_file.name.endswith('.bd')
        data = _readSQL(uploaded_file) 
        
    return data

#Métodos 'privados' de la función readFiles()

def _readCSV(path:str) -> pd.DataFrame:
    """Input: 
    path: CSV file path
       Output: 
    Pandas dataframe """
    return pd.read_csv(path)

def _readExcel(path:str) -> pd.DataFrame:
    """Input: 
    path: excel file path
       Output: 
    Pandas dataframe """
    return pd.read_excel(path)

def _readSQL(uploaded_file) -> pd.DataFrame:
    """Input: 
    path: db file path
       Output: 
    Pandas dataframe """
    fp = Path(str(uuid4())) # get the path
    fp.write_bytes(uploaded_file.getvalue())
    conn = sql.connect(str(fp)) # create a connection with the database
    with conn as engine:
        tableName = (pd.read_sql_query("SELECT * FROM sqlite_master WHERE type = 'table'", engine))['name'][0]
        table = pd.read_sql_query(f"SELECT * FROM {tableName}", engine)
    # close the connection with the database to avoid create files
    conn.close()
    fp.unlink()
    return table