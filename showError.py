import streamlit as st
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def show_error(model, x, y):
    y_pred = model.predict(x)    # calculate predictions of the model

    st.subheader("Bondad de ajuste:")   # compare predictions vs reality and show the result
    st.write("Coeficiente de determinacion:", r2_score(y, y_pred))
    st.write("Error cuadrático medio:", mean_squared_error(y, y_pred))