import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st
import pandas as pd

@st.cache_resource
def modelo_regresion_simple(columnaX, columnaY):
    x = columnaX.values.reshape(-1, 1)
    y = columnaY.values
    modelo = LinearRegression()
    modelo.fit(x, y)
    coeficientes= modelo.coef_
    intercepto = modelo.intercept_
    
    # Definir colores en función de la variable dependiente
    colores = plt.cm.viridis(y / y.max())  # Utiliza el mapa de colores "viridis"

    # Visualizar el modelo de regresión lineal simple con colores diferenciados
    plt.scatter(x, y, c='blue', s=100, label='Datos')
    plt.plot(x, modelo.predict(x), color='red', linewidth=2, label='Regresión Lineal')
    
    plt.title('Modelo de Regresión Lineal Simple')
    plt.xlabel('Variable Independiente')
    plt.ylabel('Variable Dependiente')
    plt.legend()
    st.pyplot(plt)
    
    

    return modelo