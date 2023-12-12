from read_files import *
from columns import *
from regresion_simple import modelo_regresion_simple
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from multiples_variables import *
import matplotlib.pyplot as plt
import subprocess
from leer_archivos import *
from seleccionar_columnas import *
import streamlit as st
from modelos import *
import prediction as p

st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")


st.sidebar.header("Options")

data = leer_archivos()
x , y = seleccion_columnas(data)


# buttons displayed in the interface
createModelButton = st.sidebar.button("Crear y visualizar modelo") 
saveModelButton = st.sidebar.button("Guardar modelo")
makeprediction = st.sidebar.button("Hacer predicción")

if 'model' not in st.session_state:
    st.session_state.model = None
if 'modelCreated' not in st.session_state:
    st.session_state.modelCreated = False

if 'prediction' not in st.session_state:
     st.session_state.prediction = None
if 'predictionCreated' not in st.session_state:
     st.session_state.predictionCreated = False

if createModelButton or st.session_state.modelCreated:
    st.session_state.model = crearModelo(data,x,y)
    st.session_state.modelCreated = True

if makeprediction or st.session_state.predictionCreated:
        st.session_state.predictionCreated = True
        if st.session_state.modelCreated:
            modelo = st.session_state.model
            p.prediction(modelo, x)


if saveModelButton:
    if st.session_state.modelCreated:
        pass # implment "save model" saving st.session_state.model
    else:
        st.error("No has creado ningún modelo")




