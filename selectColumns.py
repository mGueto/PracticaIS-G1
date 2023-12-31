from readFiles import *
import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer

def selection_columns(data):
    numeric_columns = select_columns(data)      # Check for numeric columns

    imputer = SimpleImputer(strategy = 'median')
    data[numeric_columns] = imputer.fit_transform(data[numeric_columns])

    st.write("Primeros registros del conjunto de datos:")
    st.write(data.head())   # Header of the dataframe is shown

    st.sidebar.subheader("Seleccione las variables independientes y la variable objetivo:") # In the sidebar, the user selects the independent variables and the target variable
    x = st.sidebar.multiselect("Variables independientes", numeric_columns) # Is allowed to use one or more independent variables, to make simple or multiple lineal regression
    y = st.sidebar.selectbox("Variable objetivo", numeric_columns)  # Select the dependet variable
    
    return x, y, False


def select_columns(df) -> tuple:
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    return num_cols