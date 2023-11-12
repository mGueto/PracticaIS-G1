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



# Esto crea un botón para cargar archivos en la barra lateral de la aplicación. uploaded_file contendrá el archivo cargado y se verifica si es None. Se muestra el nombre del archivo cargado (que es un objeto de la clase UploadedFile) usando st.write.
# FILE READING
uploaded_file = st.sidebar.file_uploader("Load file (CSV, Excel or SQLite)", type=["csv", "xlsx", "db", "sqlite"])
st.write("filename:", uploaded_file)
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
    numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
    non_numeric_columns = data.select_dtypes(exclude=['int64', 'float64']).columns


    # Se utiliza SimpleImputer de scikit-learn para imputar la media en las columnas numéricas del DataFrame donde haya valores nulos (sustituye los NULL por la media númerica, solo en las variables numericas)
    imputer = SimpleImputer(strategy='median')
    data[numeric_columns] = imputer.fit_transform(data[numeric_columns])

    # Se muestran los primeros registros del conjunto de datos después de la imputación de la media.
    ## Show
    st.write("Primeros registros del conjunto de datos:")
    st.write(data.head())

    # En la barra lateral, el usuario selecciona las variables independientes y la variable objetivo.
    ## Variable selection
    st.sidebar.subheader("Seleccione las variables independientes y la variable objetivo:")
    X = st.sidebar.multiselect("Variables independientes", numeric_columns) # Permitimos seleccionar varias columnas de variables independiente, para permitir la regresión simple (1 variable) y la regresión múltiple (+1 variable)
    y = st.sidebar.selectbox("Variable objetivo", numeric_columns) # Esto se puede ajustar para permitir en vez de una sola variables objetivo, varias. Con multiselect, igual que se hace con las variables independientes (aunque eso está fuera de la práctica, solo quiere regresión múltiple, creo)

    # Se utiliza train_test_split para dividir el conjunto de datos en conjuntos de entrenamiento y prueba.
    ## División del conjunto de datos en entrenamiento y prueba
    test_size = st.sidebar.slider("Tamaño del conjunto de prueba", 0.1, 0.9, 0.2) # Se crea un control deslizante en la barra lateral. El control deslizante permite al usuario ajustar el tamaño del conjunto de prueba. El rango es de 0.1 a 1.0 y el valor predeterminado es 0.2. El tamaño del conjunto de prueba es la proporción del conjunto de datos que se utilizará para evaluar el rendimiento del modelo después de entrenarlo.
    random_state = st.sidebar.number_input("Semilla aleatoria", value=42)

    # Esta línea utiliza st.sidebar.number_input para crear una entrada de número en la barra lateral. 
    # Permite al usuario especificar una semilla aleatoria. La semilla aleatoria se utiliza para garantizar que la división del conjunto de datos sea reproducible. 
    # Si se utiliza la misma semilla, la división será la misma en ejecuciones posteriores. 
    # Es decir, lo que hace una vez cogida la partición con el control deslizante, por cada semilla se seleccionan números aleatorios con los que entrenar el modelo.

    if X is not None and y is not None:
        #!!!! DA UN ERROR EN test_size cuando el deslizador llega a 1.0, esto es debido a que coge un conjunto de pruebas, y train_test_split no está pensada para cargar todo el conjunto de datos, para sería mejor añadir una opción extra
        # https://github.com/scikit-learn/scikit-learn/issues/20276#issuecomment-862667965
        # https://github.com/scikit-learn/scikit-learn/issues/20276#issuecomment-863215009
        X_train, X_test, y_train, y_test = train_test_split(data[X], data[y], test_size=test_size, random_state=random_state) # Esta línea utiliza la función train_test_split de scikit-learn para dividir el conjunto de datos en conjuntos de entrenamiento y prueba.
        # La razón para dividir el conjunto de datos es evaluar la capacidad del modelo para generalizar a datos no vistos. 
        # El modelo se entrena en el conjunto de entrenamiento y se evalúa en el conjunto de prueba para estimar su rendimiento en situaciones del mundo real. 
        # Esto es esencial para evitar sobreajuste (overfitting) y asegurar que el modelo sea capaz de hacer predicciones precisas en datos que no ha visto durante el entrenamiento.
        
        st.write("Información de depuración:")
        st.write(X_train.head())  # Imprime las primeras filas de X_train
        st.write(y_train.head())  # Imprime las primeras filas de y_train

        if X_train.empty:
            st.warning("X_train está vacío. Asegúrate de seleccionar variables independientes.")
        else:
            # Se crea un modelo de regresión lineal y se entrena con los datos de entrenamiento.
            ## Crear y entrenar el modelo de regresión lineal
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Se utilizan las variables independientes del conjunto de prueba para hacer predicciones con el modelo entrenado.
            ## Realizar predicciones en el conjunto de prueba
            y_pred = model.predict(X_test)

            # Se muestran métricas de rendimiento, en este caso, el error cuadrático medio.
            ## Mostrar métricas de rendimiento
            st.subheader("Métricas de rendimiento:")
            st.write("Error cuadrático medio:", mean_squared_error(y_test, y_pred))

            # Se muestra una gráfica de dispersión con los datos reales y la línea de regresión generada por el modelo.
            # Ahora solo funciona cuando elijes una sola variable independiente, cuando elijes más, este método no funciona ya que los tamaños de x e y varían
            #X corresponderá al nombre de una columna en tu conjunto de datos y habrá que iterar sobre ella:
            st.write("X:",X)
            ## Mostrar una gráfica de regresión
            st.subheader("Gráfica de Regresión Lineal")
            plt.scatter(X_test, y_test, color='blue', label='Datos reales')
            plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regresión lineal')
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
                st.write("Predicción:", prediction)
    else:
        st.info("Elegir las variables independientes y objetivo para continuar")

else:
    st.info("Carga datos para continuar.")

