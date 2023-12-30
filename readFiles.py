import pandas as pd
import sqlite3 as sql
from pathlib import Path
from uuid import uuid4

def read_files(uploaded_file):

    if uploaded_file.name.endswith('.csv'):
        data = _read_csv(uploaded_file) 
    elif uploaded_file.name.endswith('.xlsx'):
        data = _read_excel(uploaded_file)
    else:
        uploaded_file.name.endswith('.bd')
        data = _read_sql(uploaded_file) 
        
    return data

# Private methods for file reading

def _read_csv(path) -> pd.DataFrame:
    return pd.read_csv(path)

def _read_excel(path) -> pd.DataFrame:
    return pd.read_excel(path)

def _read_sql(uploaded_file) -> pd.DataFrame:
    fp = Path(str(uuid4())) # get the path
    fp.write_bytes(uploaded_file.getvalue())
    conn = sql.connect(str(fp)) # create a connection with the database
    
    with conn as engine:
        table_name = (pd.read_sql_query("SELECT * FROM sqlite_master WHERE type = 'table'", engine))['name'][0]
        table = pd.read_sql_query(f"SELECT * FROM {table_name}", engine)

    conn.close()    # close the connection with the database to avoid creation of files
    fp.unlink()

    return table