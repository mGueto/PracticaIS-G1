from read_files import *
from columns import *
from regresion_simple import modelo_regresion_simple
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from multiples_variables import *
import matplotlib.pyplot as plt
import subprocess
from leer_archivos import *
import leer_archivos as l
import streamlit as st
import seleccionar_columnas as s
import modelos as m
import showError as e
from copy import deepcopy

st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")


st.sidebar.header("Options")

data = l.leer_archivos()
x , y = s.seleccion_columnas(data)


# buttons displayed in the interface
createModelButton = st.sidebar.button("Crear y visualizar modelo") 
saveModelButton = st.sidebar.button("Guardar modelo")
deleteModelButton = st.sidebar.button("Borrar modelo")

if 'model' not in st.session_state:
    st.session_state.model = None
if 'modelCreated' not in st.session_state:
    st.session_state.modelCreated = False

            

if createModelButton or (st.session_state.modelCreated and not deleteModelButton):
    st.session_state.model = m.crearModelo(data,x,y)
    st.session_state.modelCreated = True
    e.showError(st.session_state.model, data[x], data[y]) # maybe x should be equal to data[x] 

if saveModelButton:
    if st.session_state.modelCreated:
        pass # implment "save model" saving st.session_state.model
    else:
        st.error("No has creado ningún modelo")

if deleteModelButton:
    st.session_state.model = None
    st.session_state.modelCreated = False

    



