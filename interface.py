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

st.header("Training and prediction of linear regression models")
st.title("Linear regression tool")


st.sidebar.header("Options")

data = l.leer_archivos()
x , y = s.seleccion_columnas(data)
if st.sidebar.button("Crear y visualizar modelo"):
    modelo = m.crearModelo(data,x,y)





