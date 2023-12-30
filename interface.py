from readFiles import *
import selectColumns as s
import streamlit as st
from modelOperations import *
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

st.header("Entrenamiento y predicción de modelos de regresión lineal")
st.title("Herramienta de regresión lineal")

st.sidebar.header("Cargar modelo")  # Allow the user to upload a model file
uploaded_file = st.sidebar.file_uploader("Cargar modelo archivo .pkl", type = ["pkl", "pickle"])

if uploaded_file is not None:
    try:        # Load the model from the uploaded file
        st.session_state.modelLoaded = True
        model = pickle.load(uploaded_file)
        p.prediction(model)
    except Exception as e:
        st.error("An error ocurred while loading file: " + str(e))

#________________________________________________________________________________________________________________________________________________________________________________________________
st.sidebar.header("Cargar datos")
data = None # Initialization
uploaded_file = st.sidebar.file_uploader("Cargar archivo (csv, xlsx, db, sqlite)", type = ["csv", "xlsx", "db", "sqlite"])
st.write(uploaded_file)

if uploaded_file is not None:
    try:
        data = read_files(uploaded_file)
    except Exception as e:
        st.error("An error ocurred while loading file: " + str(e))


if data is not None:    # The file must be loaded for variables to be selected
    x, y, st.session_state.modelCreated = s.selectionColumns(data)
    st.write(x)
    st.write(y)

    
    if len(x) > 0:  # There must be variables selected for the 'Create Model' button to be displayed
    
        # Buttons are displayed after uploading data
        create_model_button = st.sidebar.button("Crear y visualizar modelo")
        
        if create_model_button or (st.session_state.modelCreated):
            st.session_state.model = create_model(data,x,y) 
        
        if st.session_state.model is not None:
            model = st.session_state.model
            data_x, data_y = data[x], data[y]
            pm.plot_model(model, data_x, data_y) 
            model.set_data(x, y)
            download_button(model)
            p.prediction(model)
            e.show_error(model, data_x, data_y)  