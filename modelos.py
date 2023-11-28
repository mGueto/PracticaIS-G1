from read_files import *
from columns import *
from regresion_simple import modelo_regresion_simple
from regresion_multiple import modelo_regresion_multiple
from guardar_cargar_archivos import *
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from multiples_variables import *
import matplotlib.pyplot as plt
import subprocess
from leer_archivos import *
import leer_archivos as l
import streamlit as st
from seleccionar_columnas import *
import seleccionar_columnas as s

def modelos(data, x, y):



    if x is not None and y is not None:
            x, y = data[x], data[y]

            
            if x.shape[1] == 1:
                model = modelo_regresion_simple(x, y)
            else:
                model = modelo_regresion_multiple(x, y)

    return model   