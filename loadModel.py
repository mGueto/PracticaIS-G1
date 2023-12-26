import streamlit as st
import pickle
import prediction as p

def loadModel():
    st.session_state.modelLoaded = True
    uploaded_file = st.sidebar.file_uploader("Cargar archivo .pkl", type=["pkl", "pickle"])
    if uploaded_file is not None:
        try:
            # Load the model from the uploaded file
            modelo = pickle.load(uploaded_file)
            p.prediction(modelo)
        except Exception as e:
            st.error("An error ocurred while loading file: " + str(e))