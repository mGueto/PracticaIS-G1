from sklearn.linear_model import LinearRegression
import streamlit as st
import pandas as pd
from class_customModelo import CustomModelo
import pickle



def save_object(path, obj):
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
        save_object("model_to_save.pickle", modelo)
        with open("model_to_save.pickle", "rb") as file:

            if st.sidebar.download_button(
                    label="Descargar modelo",
                    data=file,
                    file_name="model.pickle",
                    mime="pickle/pickle"):
                st.sidebar.write("Se ha guardado correctamente el modelo. ¡Revise descargas!")
    except:
        st.write("¡Error! No se puedo guardar el modelo")