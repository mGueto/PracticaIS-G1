import streamlit as st
import joblib
import os

def saveModel(model, path):
    """
    
    """
    try:
        joblib.dump(model, path)
        st.success("Modelo guardado exitosamente.")
    except Exception as e:
        st.error(f"Error al guardar el modelo: {e}")

def loadModel(path):
    try:
        modelo = joblib.load(path)
        st.success("Modelo cargado exitosamente.")
        return modelo
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None