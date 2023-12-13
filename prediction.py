from interface import *
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

def prediction(modelo,x):
    x = data[x]
    if x.shape[1] == 1:

        valor_prediccion = st.sidebar.number_input(f"Ingrese un valor para {x.columns[0]}")
        prediccion = modelo.predict([[valor_prediccion]])
        st.sidebar.subheader("Resultado de la Predicción:")
        st.sidebar.write(f"Predicción: {prediccion[0]}")
    
    else:
        st.sidebar.subheader("Predicción multiple")
        valor_prediccion = {}
        for columna in x.columns:
            valor = st.sidebar.number_input(f"Ingrese un valor para {columna}")
            valor_prediccion[columna] = valor
        
        # Convierte el diccionario de valores a un DataFrame para la predicción
        input_data = pd.DataFrame([valor_prediccion])
        prediccion = modelo.predict(input_data)
        
        st.sidebar.subheader("Resultado de la Predicción:")
        st.sidebar.write(f"Predicción: {prediccion[0]}")
