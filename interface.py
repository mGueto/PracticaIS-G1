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

# Use the command «streamlit run interface.py --server.port=8080 --browser.serverAddress='127.0.0.1'» to run the app

# APPEARANCE

## Header
st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")

## Sidebar
st.sidebar.header("Options")




# FILE READING
uploaded_file = st.sidebar.file_uploader("Load file (CSV, Excel or SQLite)", type=["csv", "xlsx", "db", "sqlite"])
st.write("filename:", uploaded_file)
data = None

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            data = readCSV(uploaded_file) 
        elif uploaded_file.name.endswith('.xlsx'):
            data = readExcel(uploaded_file)
        else:
            data = readSQL('data/' + uploaded_file.name)
    except Exception as e:
        st.error("An error ocurred while loading file: " + str(e))
    
            

## Check for loaded data
if data is not None and not data.empty:

    ### Check for numeric columns
    numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
    non_numeric_columns = data.select_dtypes(exclude=['int64', 'float64']).columns
else:
    st.info("Carga datos para continuar.")


# Imputar la media solo en las columnas numéricas
imputer = SimpleImputer(strategy='mean')
data[numeric_columns] = imputer.fit_transform(data[numeric_columns])

# Show
st.write("Primeros registros del conjunto de datos:")
st.write(data.head())

# Selección de variables
st.sidebar.subheader("Seleccione las variables independientes y la variable objetivo:")
X = st.sidebar.multiselect("Variables independientes", numeric_columns)
y = st.sidebar.selectbox("Variable objetivo", numeric_columns)

# División del conjunto de datos en entrenamiento y prueba
test_size = st.sidebar.slider("Tamaño del conjunto de prueba", 0.1, 1.0, 0.2)
random_state = st.sidebar.number_input("Semilla aleatoria", value=42)

X_train, X_test, y_train, y_test = train_test_split(data[X], data[y], test_size=test_size, random_state=random_state)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Mostrar métricas de rendimiento
st.subheader("Métricas de rendimiento:")
st.write("Error cuadrático medio:", mean_squared_error(y_test, y_pred))

# Mostrar una gráfica de regresión
st.subheader("Gráfica de Regresión Lineal")
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regresión lineal')
plt.xlabel("Variable Independiente")
plt.ylabel("Variable Objetivo")
plt.legend()
st.pyplot(plt)

# Guardar el modelo
if st.sidebar.button("Guardar modelo"):
    joblib.dump(model, "modelo.pkl")
    st.success("Modelo guardado con éxito")

# Hacer predicciones con el modelo guardado
if st.sidebar.checkbox("Hacer predicciones con el modelo guardado"):
    loaded_model = joblib.load("modelo.pkl")
    st.subheader("Hacer predicciones:")
    input_data = {}
    for variable in X:
        input_data[variable] = st.number_input(f"Ingrese el valor de {variable}")
    prediction = loaded_model.predict(pd.DataFrame([input_data]))
    st.write("Predicción:", prediction)
