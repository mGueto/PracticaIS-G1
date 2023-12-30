from readFile import *
from readFiles import *
import selectColumns as s
from columns import *
from class_customModel import CustomModel
from regresionSimple import regresionSimpleModel
from regresionMultiple import *
from loadModel import loadModel
from saveModel import downloadButton
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import subprocess
import streamlit as st
import createModel as m
import showError as e
import prediction as p
import pickle
import plotModel as pm



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

#________________________________________________________________________________________________________________________________________________________________________________________________
st.sidebar.header("Cargar datos")
data = None # Al principio definimos las variables que se irán modificando para que la
uploaded_file = st.sidebar.file_uploader("Cargar archivo (csv, xlsx, db, sqlite)", type=["csv", "xlsx", "db", "sqlite"])
st.write(uploaded_file)
if uploaded_file is not None:
    try:
        data = ReadFiles(uploaded_file)
    except Exception as e:
        st.error("An error ocurred while loading file: " + str(e))

# The file must be loaded for variables to be selected.
if data is not None:
    x, y, st.session_state.modelCreated = s.selectionColumns(data)
    st.write(x)
    st.write(y)

    # There must be variables selected for the 'Create Model' button to be displayed.
    if len(x)>0:
    
        # buttons displayed after uploading data
        createModelButton = st.sidebar.button("Crear y visualizar modelo")
        
        if createModelButton or (st.session_state.modelCreated):
            st.session_state.model = m.createModel(data,x,y) 
        if st.session_state.model is not None:
            modelo = st.session_state.model
            dataX, dataY = data[x], data[y]
            pm.plotModel(modelo, dataX, dataY) 
            modelo.set_data(x, y)
            downloadButton(modelo)
            p.prediction(modelo)
            e.showError(modelo, dataX, dataY)  