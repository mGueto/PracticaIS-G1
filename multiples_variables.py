from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import streamlit as st

# very slow (create a new model for each variable), improvable

def regresion_entre_variables(columnaX, columnaY):

    resultados = []
    for columna_independiente in columnaX.columns:
        print(columna_independiente, '\n', '#'*10, columnaX.columns)
        # Extraer las columnas correspondientes de los DataFrames
        X = columnaX[columna_independiente].values.reshape(-1, 1)
        y = columnaY.values

        # Ajustar el modelo de regresión lineal
        modelo = LinearRegression()
        modelo.fit(X, y)

        # Almacenar los resultados en la lista
        resultado = {
            'variable_dependiente': columnaY.name,
            'variable_independiente': columna_independiente,
            'coeficiente': modelo.coef_[0],
            'intercepto': modelo.intercept_
        }
        resultados.append(resultado)

        # Visualizar el modelo de regresión lineal simple con colores diferenciados
        colores = plt.cm.viridis(y / y.max())
        plt.scatter(X, y, c=colores, s=100, label='Datos')
        plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Regresión Lineal')

        plt.title(f'Regresión entre {columnaY.name} y {columna_independiente}')
        plt.xlabel(columna_independiente)
        plt.ylabel(columnaY.name)
        plt.legend()
        st.pyplot(plt) # show in interface the graphic
        plt.clf() # clear plot


    return resultados