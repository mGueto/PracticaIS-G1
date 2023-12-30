from regresionModels import *
from readFiles import *
import streamlit as st
from selectColumns import *
import pickle

def create_model(data, x, y):

        median_x = data[x].median()
        median_y = data[y].median()
        data[x] = data[x].fillna(median_x)
        data[y] = data[y].fillna(median_y)
        x, y = data[x], data[y]
        
        if x.shape[1] == 1:
            model = simple_regression_model(x, y)
            

            
        else:
            model = multiple_regression_model(x, y)
            

        
        st.write(model)
        return model  

def save_object(path, obj):
    with open(path, "wb") as f:
        pickle.dump(obj, f)

def download_button(model):
    try:
        save_object("model_to_save.pickle", model)
        with open("model_to_save.pickle", "rb") as file:
            if st.sidebar.download_button(
                    label = "Descargar modelo",
                    data = file,
                    file_name = "model.pickle",
                    mime = "pickle/pickle"):
                st.sidebar.write("Se ha guardado correctamente el modelo. ¡Revise descargas!")
    except:
        st.write("¡Error! No se puedo guardar el modelo")