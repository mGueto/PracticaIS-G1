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
from loadModel import loadModel




if 'model' not in st.session_state:
    st.session_state.model = None
if 'modelCreated' not in st.session_state:
    st.session_state.modelCreated = False
if 'modelLoaded' not in st.session_state:
    st.session_state.modelLoaded = False



st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")

# Allow the user to upload a model file
st.sidebar.header("Cargar modelo")
uploaded_file = st.sidebar.file_uploader("Cargar modelo archivo .pkl", type=["pkl", "pickle"])
if uploaded_file is not None:
    try:
        # Load the model from the uploaded file
        st.session_state.modelLoaded = True
        modelo = pickle.load(uploaded_file)
        p.prediction(modelo)
    except Exception as e:
        st.error("An error ocurred while loading file: " + str(e))

st.sidebar.header("Cargar datos")
data = leer_archivos()

# The file must be loaded for variables to be selected.
if data is not None:
    x, y, st.session_state.modelCreated = s.seleccion_columnas(data)

    # There must be variables selected for the 'Create Model' button to be displayed.
    if len(x)>0:
    
        # buttons displayed after uploading data
        createModelButton = st.sidebar.button("Crear y visualizar modelo")
        
        if createModelButton or (st.session_state.modelCreated):
            st.session_state.model = m.crearModelo(data,x,y)
            st.session_state.modelCreated = True
            modelo = st.session_state.model
            modelo.set_data(x, y)
            downloadButton(modelo)
            p.prediction(modelo)
            e.showError(modelo, data[x], data[y]) # maybe x should be equal to data[x] 