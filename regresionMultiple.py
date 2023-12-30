from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import streamlit as st
from class_customModel import CustomModel

# very slow (create a new model for each variable), improvable

def regresionMultipleModel(columnas_X, columna_Y):
    # Tomar un subconjunto más pequeño de los datos

    X = columnas_X
    y = columna_Y
    
    # Entrenar el modelo de regresión
    modelo = CustomModel()
    modelo.fit(X, y)
    coeficientes = modelo.coef_
    intercepto = modelo.intercept_

    for i, columna in enumerate(X.columns):
            predicciones = intercepto + coeficientes[i] * X[columna]
            # Visualizar los datos y la predicción
            plt.scatter(X[columna], y, label=f'Datos')
            plt.plot(X[columna], predicciones, label=f'Predicción ({columna})', color='red')
            plt.xlabel(columna)
            plt.ylabel(y.name)  # Suponemos que df_Y tiene una sola columna
            plt.legend()
            plt.show()
            st.pyplot(plt)
            plt.clf()
            
    return modelo