import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression



def modelo_regresion_multiple_3d(columnas_X, columna_Y):
    # Tomar un subconjunto más pequeño de los datos

    X = columnas_X.values
    y = columna_Y.values
    
    # Entrenar el modelo de regresión
    modelo = LinearRegression()
    modelo.fit(X, y)
    
    # Crear una malla 3D
   # x1, x2 = np.meshgrid(X[:,0], X[:,1])
    x1 = np.linspace(X[:,0].min(), X[:,0].max(), num=50)
    x2 = np.linspace(X[:,1].min(), X[:,1].max(), num=50)
    x1, x2 = np.meshgrid(x1, x2)
    y_pred = modelo.predict(np.c_[x1.ravel(), x2.ravel()]).reshape(x1.shape)
    
    # Visualizar el plano de regresión en 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Graficar los datos reales con etiqueta personalizada
    ax.scatter(X[:,0], X[:,1], y, c='steelblue', label='Datos reales', alpha=0.7)
    
    # Graficar el plano de regresión con etiquetas personalizadas
    surf = ax.plot_surface(x1, x2, y_pred, cmap='viridis', alpha=0.5, label='Plano de Regresión')
    
    # Obtener los nombres de las columnas de las variables independientes
    variable1_name, variable2_name = columnas_X.columns[0], columnas_X.columns[1]
    
    ax.set(xlabel=variable1_name, ylabel=variable2_name, zlabel=columna_Y.name)
    
    # Ajustar la posición de la barra de color
    cbar = fig.colorbar(surf, shrink=0.5, aspect=10, pad=0.15)
    
    plt.title('Modelo de Regresión Lineal Múltiple en 3D')
    plt.show()

    return modelo






