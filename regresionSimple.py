import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st
import pandas as pd
from class_customModel import CustomModel

def regresionSimpleModel(columnaX, columnaY):
    x = columnaX.values
    y = columnaY.values
    modelo = CustomModel()
    modelo.fit(x, y)
    
    

    return modelo