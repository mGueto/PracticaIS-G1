import streamlit as st
import pandas as pd

def prediction(model):
    if len(model.columns_x) == 1:
    

        prediction_value = st.sidebar.number_input(f"Ingrese un valor para {model.columns_x[0]}")
        prediction = model.predict([[prediction_value]])
        st.sidebar.subheader("Resultado de la Predicción:")
        st.sidebar.write(f"Predicción para {model.columns_y}: {prediction[0]}")
    
    else:
        st.sidebar.subheader("Predicción multiple")
        prediction_value = {}

        for column in model.columns_x[:]:
            value = st.sidebar.number_input(f"Ingrese un valor para {column}")
            prediction_value[column] = value

        # Convierte el diccionario de valores a un DataFrame para la predicción
        input_data = pd.DataFrame([prediction_value])
        prediction = model.predict(input_data)

        st.sidebar.subheader("Resultado de la Predicción:")
        st.sidebar.write(f"Predicción para {model.columns_y}: {prediction[0]}")

