import streamlit as st
import joblib
import os

def SaveModel(model, rute):
    """
    
    """
    try:
        joblib.dump(model, rute)
        st.success("Modelo guardado exitosamente.")
    except Exception as e:
        st.error(f"Error al guardar el modelo: {e}")

def LoadModel(rute):
    try:
        modelo = joblib.load(rute)
        st.success("Modelo cargado exitosamente.")
        return modelo
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None
    