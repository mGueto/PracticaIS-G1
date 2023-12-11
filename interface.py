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
import leer_archivos as l
import streamlit as st
import seleccionar_columnas as s
import modelos as m

st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")


st.sidebar.header("Options")

data = l.leer_archivos()
x , y = s.seleccion_columnas(data)


# buttons displayed in the interface
createModelButton = st.sidebar.button("Crear y visualizar modelo") 

if 'model' not in st.session_state:
    st.session_state.model = None
if 'modelCreated' not in st.session_state:
    st.session_state.modelCreated = False
            

if createModelButton or st.session_state.modelCreated:
    st.session_state.model = m.crearModelo(data,x,y)
    st.session_state.modelCreated = True
    downloadButton(st.session_state.model)
