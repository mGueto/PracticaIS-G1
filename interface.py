from read_files import *
from columns import *
from regresion_simple import modelo_regresion_simple
from regresion_multiple import modelo_regresion_multiple_3d


import streamlit as st
"""import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
import joblib
import matplotlib.pyplot as plt"""
"""from contextlib import contextmanager
from pathlib import Path
from uuid import uuid4"""

# Use the command «streamlit run interface.py --server.port=8080 --browser.serverAddress='127.0.0.1'» to run the interface

# APPEARANCE

# Estas líneas son para mostrar encabezados en la interfaz de la aplicación. st.header muestra un encabezado más grande y st.title muestra un título.
## Header
st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")

# Aquí se define un encabezado en la barra lateral de la interfaz de la aplicación.
## Sidebar
st.sidebar.header("Options")



# Esto crea un botón para cargar archivos en la barra lateral de la aplicación. uploaded_file contendrá el archivo cargado y se verifica si es None. Se muestra el nombre del archivo cargado (que es un objeto de la clase UploadedFile) usando st.write.
# FILE READING
uploaded_file = st.sidebar.file_uploader("Load file (CSV, Excel or SQLite)", type=["csv", "xlsx", "db", "sqlite"])
st.write("filename:", uploaded_file.name)
data = None # Al principio definimos las variables que se irán modificando para que la aplicación no de errores al intentar comparar valores que no existen.

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
    
            
# Se verifica si se ha cargado algún dato y si el DataFrame no está vacío. Si es así, se obtienen las columnas numéricas y no numéricas. Si no hay datos, se muestra un mensaje informativo.
## Check for loaded data
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

  
    if x is not None and y is not None:
        x, y = data[x], data[y]

        
        if x.shape[1] == 1:
            modelo_regresion_simple(x, y)
        else:
            modelo_regresion_multiple_3d(x, y)
       
        """st.write("Información de depuración:")
        st.write(x.head())  # Prints the firsts rows of X
        st.write(y.head())  # Prints the firsts rows of y

        if x.empty:
            st.warning("X_train está vacío. Asegúrate de seleccionar variables independientes.")
        else:
            # Create the lineal regression model
            model = LinearRegression()
            model.fit(x, y)

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
                loaded_model = joblib.load("modelo.pkl")
                st.subheader("Hacer predicciones:")
                input_data = {}
                for variable in X:
                    input_data[variable] = st.number_input(f"Ingrese el valor de {variable}")
                prediction = loaded_model.predict(pd.DataFrame([input_data]))
                st.write("Predicción:", prediction)"""
    else:
        st.info("Elegir las variables independientes y objetivo para continuar")

else:
    st.info("Carga datos para continuar.")

