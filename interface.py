from read_files import *
from select_columns import *


import streamlit as st
import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
import joblib
import matplotlib.pyplot as plt
from contextlib import contextmanager
from pathlib import Path
from uuid import uuid4

# Use the command «streamlit run interface.py --server.port=8080 --browser.serverAddress='127.0.0.1'» to run the interface

# APPEARANCE

# Estas líneas son para mostrar encabezados en la interfaz de la aplicación. st.header muestra un encabezado más grande y st.title muestra un título.
## Header
st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")

# Aquí se define un encabezado en la barra lateral de la interfaz de la aplicación.
## Sidebar
st.sidebar.header("Options")

# Esto crea un botón para cargar archivos en la barra lateral de la aplicación. uploadedFile contendrá el archivo cargado y se verifica si es None. Se muestra el nombre del archivo cargado (que es un objeto de la clase UploadedFile) usando st.write.
# FILE READING
uploadedFile = st.sidebar.file_uploader("Load file (CSV, Excel or SQLite)", type=["csv", "xlsx", "db", "sqlite"])
st.write("filename:", uploadedFile.name)
data = None # Al principio definimos las variables que se irán modificando para que la aplicación no de errores al intentar comparar valores que no existen.

# Aquí se intenta leer el archivo cargado dependiendo de su extensión. Se manejan posibles excepciones y se muestra un mensaje de error si ocurre alguna.
if uploadedFile is not None:
    try: # Se llaman a las funciones de readFiles
        if uploadedFile.name.endswith('.csv'):
            data = readCSV(uploadedFile) 
        elif uploadedFile.name.endswith('.xlsx'):
            data = readExcel(uploadedFile)
        else:
            data = readSQL(uploadedFile)

    except Exception as e:
        st.error("An error ocurred while loading file: " + str(e))
    
            
# Se verifica si se ha cargado algún dato y si el DataFrame no está vacío. Si es así, se obtienen las columnas numéricas y no numéricas. Si no hay datos, se muestra un mensaje informativo.
## Check for loaded data
if data is not None:

    ### Check for numeric columns
    numericColumns = data.select_dtypes(include=['int64', 'float64']).columns
    nonNumericColumns = data.select_dtypes(exclude=['int64', 'float64']).columns

    # Se utiliza SimpleImputer de scikit-learn para imputar la media en las columnas numéricas del DataFrame donde haya valores nulos (sustituye los NULL por la media númerica, solo en las variables numericas)
    imputer = SimpleImputer(strategy='median')
    data[numericColumns] = imputer.fit_transform(data[numericColumns])

    # Se muestran los primeros registros del conjunto de datos después de la imputación de la media.
    ## Show
    st.write("Primeros registros del conjunto de datos:")
    st.write(data.head())

    # In the sidebar, the user selects the independent variables and the target variable.
    ## Variable selection
    st.sidebar.subheader("Seleccione las variables independientes y la variable objetivo:")
    # Is allowed to use one or more independent variables, to make simple or multiple lineal regression
    X = st.sidebar.multiselect("Variables independientes", numericColumns) 
    # Select the dependet variable
    y = st.sidebar.selectbox("Variable objetivo", numericColumns) 

    if X is not None and y is not None:
        X, y = data[X], data[y]
        st.write("Información de depuración:")
        st.write(X.head())  # Prints the firsts rows of X
        st.write(y.head())  # Prints the firsts rows of y

        if X.empty:
            st.warning("X_train está vacío. Asegúrate de seleccionar variables independientes.")
        else:
            # Create the lineal regression model
            model = LinearRegression()
            model.fit(X, y)

            # Predictions based in the model
            y_pred = model.predict(X)

            # show mean square error:
            st.subheader("Métricas de rendimiento:")
            # real values vs predicted values
            st.write("Error cuadrático medio:", mean_squared_error(y, y_pred))

            # Se muestra una gráfica de dispersión con los datos reales y la línea de regresión generada por el modelo.
            # Ahora solo funciona cuando elijes una sola variable independiente, cuando elijes más, este método no funciona ya que los tamaños de x e y varían
            
            ## Mostrar una gráfica de regresión
            st.subheader("Gráfica de Regresión Lineal")
            plt.scatter(X, y, color='blue', label='Datos reales')
            plt.plot(X, y_pred, color='red', linewidth=2, label='Regresión lineal')
            plt.xlabel("Variable Independiente")
            plt.ylabel("Variable Objetivo")
            plt.legend()
            st.pyplot(plt)

            # Si se presiona el botón en la barra lateral, se guarda el modelo entrenado en un archivo llamado "modelo.pkl".
            ## Guardar el modelo (Está aún por desarrollar)
            if st.sidebar.button("Guardar modelo"):
                joblib.dump(model, "modelo.pkl")
                st.success("Modelo guardado con éxito")
            
            # Si se selecciona la casilla de verificación en la barra lateral, se cargará el modelo guardado y se permitirá al usuario ingresar valores para hacer predicciones con el modelo. La predicción resultante se muestra en la interfaz.
            ## Hacer predicciones con el modelo guardado
            if st.sidebar.checkbox("Hacer predicciones con el modelo guardado"):
                loadedModel = joblib.load("modelo.pkl")
                st.subheader("Hacer predicciones:")
                inputData = {}
                for variable in X:
                    inputData[variable] = st.number_input(f"Ingrese el valor de {variable}")
                prediction = loadedModel.predict(pd.DataFrame([inputData]))
                st.write("Predicción:", prediction)
    else:
        st.info("Elegir las variables independientes y objetivo para continuar")

else:
    st.info("Carga datos para continuar.")
