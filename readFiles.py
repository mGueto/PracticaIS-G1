from readFile import _readCSV, _readExcel, _readSQL
from columns import *
from regresionModels import *
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import subprocess
import prediction as p
import pickle

import streamlit as st

#Las funciones internas son privadas ya que solo se usan dentro de esa función
def ReadFiles(uploaded_file):

    if uploaded_file.name.endswith('.csv'):
        data = _readCSV(uploaded_file) 
    elif uploaded_file.name.endswith('.xlsx'):
        data = _readExcel(uploaded_file)
    else:
        uploaded_file.name.endswith('.bd')
        data = _readSQL(uploaded_file) 
        
    return data