from read_files import *
from columns import *
from regresion_simple import modelo_regresion_simple
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from multiples_variables import *
import matplotlib.pyplot as plt
import subprocess
from save_models import downloadButton
from leer_archivos import *
import streamlit as st
import seleccionar_columnas as s
import modelos as m
import showError as e
import prediction as p
import pickle
from class_customModelo import CustomModelo

st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")


st.sidebar.header("Options")

data = leer_archivos()
x , y = s.seleccion_columnas(data)


# buttons displayed in the interface
createModelButton = st.sidebar.button("Crear y visualizar modelo") 
loadModelButton = st.sidebar.button("Cargar modelo") 


if 'model' not in st.session_state:
    st.session_state.model = None
if 'modelCreated' not in st.session_state:
    st.session_state.modelCreated = False
if 'modelLoaded' not in st.session_state:
    st.session_state.modelLoaded = False


            

if createModelButton or (st.session_state.modelCreated):
    st.session_state.model = m.crearModelo(data,x,y)
    st.session_state.modelCreated = True
    modelo = st.session_state.model
    modelo.set_data(x, y)
    p.prediction(modelo)
    downloadButton(modelo)
    e.showError(modelo, data[x], data[y]) # maybe x should be equal to data[x] 



if loadModelButton or st.session_state.modelLoaded:
    # Allow the user to upload a model file
    st.session_state.modelLoaded = True
    uploaded_file = st.file_uploader("Cargar archivo .pkl", type=["pkl", "pickle"])
    if uploaded_file is not None:
        try:
            # Load the model from the uploaded file
            modelo = pickle.load(uploaded_file)
            p.prediction(modelo)
        except Exception as e:
            st.error("An error ocurred while loading file: " + str(e))

    


