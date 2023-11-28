from read_files import *
from columns import *
from regresion_simple import modelo_regresion_simple
from regresion_multiple import modelo_regresion_multiple
from guardar_cargar_archivos import *
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from multiples_variables import *
import matplotlib.pyplot as plt
import subprocess
from leer_archivos import *
import leer_archivos as l
import streamlit as st

def seleccion_columnas(data):

    if data is not None:

        ### Check for numeric columns
        numeric_columns = select_columns(data)

        # Se utiliza SimpleImputer de scikit-learn para imputar la media en las columnas numéricas del DataFrame donde haya valores nulos (sustituye los NULL por la media númerica, solo en las variables numericas)
        """imputer = SimpleImputer(strategy='median')
        data[numeric_columns] = imputer.fit_transform(data[numeric_columns])"""

        # Se muestran los primeros registros del conjunto de datos después de la imputación de la media.
        ## Show
        st.write("Primeros registros del conjunto de datos:")
        st.write(data.head())

        # In the sidebar, the user selects the independent variables and the target variable.
        ## Variable selection
        st.sidebar.subheader("Seleccione las variables independientes y la variable objetivo:")
        # Is allowed to use one or more independent variables, to make simple or multiple lineal regression
        x = st.sidebar.multiselect("Variables independientes", numeric_columns) 
        # Select the dependet variable
        y = st.sidebar.selectbox("Variable objetivo", numeric_columns) 

    return x, y