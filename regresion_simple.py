import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



def modelo_regresion_simple(columnaX, columnaY):
    X = columnaX.values.reshape(-1, 1)
    y = columnaY.values
    modelo = LinearRegression()
    modelo.fit(X, y)
    
    # Definir colores en función de la variable dependiente
    colores = plt.cm.viridis(y / y.max())  # Utiliza el mapa de colores "viridis"

    # Visualizar el modelo de regresión lineal simple con colores diferenciados
    plt.scatter(X, y, c=colores, s=100, label='Datos')
    plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Regresión Lineal')
    
    plt.title('Modelo de Regresión Lineal Simple')
    plt.xlabel('Variable Independiente')
    plt.ylabel('Variable Dependiente')
    plt.legend()
    plt.show()


    return modelo
