import sqlite3
import streamlit as st
from contextlib import contextmanager
from pathlib import Path
from uuid import uuid4


@contextmanager
def sqlite_connect(db_bytes):
    fp = Path(str(uuid4()))
    fp.write_bytes(db_bytes.getvalue())
    conn = sqlite3.connect(str(fp))

    return conn 
    


db = st.file_uploader("Upload a SQLite database file.", type="db")

if db:
    with sqlite_connect(db) as conn:
        st.write("Connection object:", conn)
        # ... your code ...