from readFile import *
from regresionModels import *
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import subprocess
from readFiles import *
import readFiles as l
import streamlit as st
from selectColumns import *
import selectColumns as s
import pickle
from class_customModel import CustomModel
import pandas as pd
from sklearn.linear_model import LinearRegression

def createModel(data, x, y):

        X_mediana = data[x].median()
        Y_mediana = data[y].median()
        data[x] = data[x].fillna(X_mediana)
        data[y] = data[y].fillna(Y_mediana)
        x, y = data[x], data[y]
        
        if x.shape[1] == 1:
            modelo = regresionSimpleModel(x, y)
            

            
        else:
            modelo = regresionMultipleModel(x, y)
            

        
        st.write(modelo)
        return modelo   

def saveObject(path, obj):
    """
    input:
    path = extensión de donde guardar
    obj = objeto a guardar
    """
    with open(path, "wb") as f:
        pickle.dump(obj, f)

def downloadButton(modelo):

    """
    input = modelo

    salida = None
    """
    #intenta guardar el modelo en un archivo auxiliar,
    
    #y después procede a guardar una copia del documento en la carpeta de descargas.
    try:
        saveObject("model_to_save.pickle", modelo)
        with open("model_to_save.pickle", "rb") as file:

            if st.sidebar.download_button(
                    label="Descargar modelo",
                    data=file,
                    file_name="model.pickle",
                    mime="pickle/pickle"):
                st.sidebar.write("Se ha guardado correctamente el modelo. ¡Revise descargas!")
    except:
        st.write("¡Error! No se puedo guardar el modelo")