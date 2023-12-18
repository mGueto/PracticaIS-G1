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

st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")


st.sidebar.header("Options")

data = leer_archivos()
x , y = s.seleccion_columnas(data)


# buttons displayed in the interface
createModelButton = st.sidebar.button("Crear y visualizar modelo") 
makeprediction = st.sidebar.button("Hacer predicción")
loadModelButton = st.sidebar.button("Cargar modelo") 


if 'model' not in st.session_state:
    st.session_state.model = None
if 'modelCreated' not in st.session_state:
    st.session_state.modelCreated = False


            

if createModelButton or (st.session_state.modelCreated):
    st.session_state.model = m.crearModelo(data,x,y)
    st.session_state.modelCreated = True
    e.showError(st.session_state.model, data[x], data[y]) # maybe x should be equal to data[x] 

if 'prediction' not in st.session_state:
     st.session_state.prediction = None
if 'predictionCreated' not in st.session_state:
     st.session_state.predictionCreated = False


if makeprediction or st.session_state.predictionCreated:
    st.session_state.predictionCreated = True
    if st.session_state.modelCreated:
        modelo = st.session_state.model
        p.prediction(modelo, x)
    if st.session_state.modelCreated:
        downloadButton(st.session_state.model)

if loadModelButton:
    # Allow the user to upload a model file
    uploaded_file = st.file_uploader("Cargar archivo .pkl", type=["pkl"])
    if uploaded_file is not None:
        # Load the model from the uploaded file
        st.session_state.model = pickle.load(uploaded_file)
        st.session_state.modelCreated = True

    


