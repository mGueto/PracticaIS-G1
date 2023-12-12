import streamlit as st
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from pandas import Series, DataFrame 

def showError(model: LinearRegression, x: DataFrame, y: Series):
    """Shows in the interface the goodnes of fit (mean squared error and r^2)"""
    # calculate predictions of the model
    yPred = model.predict(x)
    # compare predictions vs reality and show the result.
    st.subheader("Bondad de ajuste:")
    st.write("Coeficiente de determinacion:", r2_score(y, yPred))
    st.write("Error cuadrático medio:", mean_squared_error(y, yPred))