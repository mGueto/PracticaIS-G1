import matplotlib.pyplot as plt
import streamlit as st

def plotModel(modelo, columnX, columnY):
    if columnX.shape[1] == 1:
        x, y = columnX.values, columnY.values
        plt.scatter(x, y, c='blue', s=100, label='Datos')
        plt.plot(x, modelo.predict(x), color='red', linewidth=2, label='Regresión Lineal')
        plt.title('Modelo de Regresión Lineal Simple')
        plt.xlabel(columnX.columns[0])
        plt.ylabel(columnY.name)
        plt.legend()
        st.pyplot(plt)
    else: 
        X = columnX
        y = columnY
        coeficientes = modelo.coef_
        intercepto = modelo.intercept_

        for i, columna in enumerate(X.columns):
                predicciones = intercepto + coeficientes[i] * X[columna]
                # Visualizar los datos y la predicción
                plt.scatter(X[columna], y, label=f'Datos')
                plt.plot(X[columna], predicciones, label=f'Predicción ({columna})', color='red')
                plt.xlabel(columna)
                plt.ylabel(y.name)  # Suponemos que df_Y tiene una sola columna
                plt.legend()
                plt.show()
                st.pyplot(plt)
                plt.clf()