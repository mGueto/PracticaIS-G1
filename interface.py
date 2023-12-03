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
import joblib



st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")

data = l.leer_archivos()
x , y = s.seleccion_columnas(data)

createModelButton = st.sidebar.button("Crear y visualizar modelo")
saveModelButton = st.sidebar.button("Guardar modelo")


if 'modelCreated' not in st.session_state:
    st.session_state.modelCreated = False

st.sidebar.header("Options")


if createModelButton or st.session_state.modelCreated:
    model = m.crearModelo(data,x,y)
    st.session_state.modelCreated = True


if saveModelButton:
    savePath = "data/model.pkl" # save in this path because pop_up_save_file makes a copy of
    #the file stored in that path
    joblib.dump(model, savePath)
    # call file pop_up_save_file.py to open a pop up window to copy model.pkl to a new destination
    subprocess.Popen(["python", "pop_up_save_file.py"])






