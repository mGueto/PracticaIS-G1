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

import streamlit as st

def leer_archivos():
    uploaded_file = st.sidebar.file_uploader("Load file (CSV, Excel or SQLite)", type=["csv", "xlsx", "db", "sqlite"])
    st.write("filename:", uploaded_file.name)
    data = None # Al principio definimos las variables que se irán modificando para que la 
    #aplicación no de errores al intentar comparar valores que no existen.

    # Aquí se intenta leer el archivo cargado dependiendo de su extensión. Se manejan posibles excepciones y se muestra un mensaje de error si ocurre alguna.
    if uploaded_file is not None:
        try: # Se llaman a las funciones de read_files

            if uploaded_file.name.endswith('.csv'):
                data = readCSV(uploaded_file) 
            elif uploaded_file.name.endswith('.xlsx'):
                data = readExcel(uploaded_file)
            else:
                data = readSQL(uploaded_file)

        except Exception as e:
            st.error("An error ocurred while loading file: " + str(e))
    return data