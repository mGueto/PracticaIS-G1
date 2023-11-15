from sklearn.linear_model import LinearRegression
import pandas as pd

def entrenarModeloRegresion(df, columnasX, columnaY):
    # Rellenar NaN en las columnas de características
    df[columnasX] = df[columnasX].apply(lambda x: x.fillna(x.median()))

    # Rellenar NaN en la columna de la variable objetivo con la mediana
    df[columnaY] = df[columnaY].fillna(df[columnaY].median())

    # Obtén las características (X) y la variable objetivo (y) del DataFrame
    X = df[columnasX]
    y = df[columnaY]
    
    # Inicializa el modelo de regresión lineal
    modelo = LinearRegression()
    
    # Ajusta el modelo a los datos
    modelo.fit(X, y)
    
    return modelo, X, y

import matplotlib.pyplot as plt
import numpy as np

def graficarPrediccion(modelo, X, y):
    # Realizar predicciones utilizando el modelo
    y_pred = modelo.predict(X)
    
    # Crear una gráfica de dispersión de los datos
    plt.scatter(X, y, label='Datos reales', color='blue')
    
    # Dibujar la línea de predicción
    plt.plot(X, y_pred, label='Predicción', color='red')
    
    # Etiquetas y leyendas
    plt.xlabel('Variable independiente')
    plt.ylabel('Variable dependiente')
    plt.legend()
    
    # Mostrar la gráfica
    plt.show()

if __name__ == "__main__":
    from read_files import readCSV
    modelM, X, y = entrenarModeloRegresion(readCSV("data/housing.csv"), ['longitude', 'latitude'], 'latitude')
    modelS, X, y = entrenarModeloRegresion(readCSV("data/housing.csv"), ['longitude'], 'latitude')

    graficarPrediccion(modelS, X, y)
