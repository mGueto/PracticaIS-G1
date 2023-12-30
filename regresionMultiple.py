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
    
    return modelo