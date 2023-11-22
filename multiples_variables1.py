from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def regresion_entre_variables(columnaX, columnaY):
    for columna_independiente in columnaX.columns:
        # Extraer las columnas correspondientes de los DataFrames
        X = columnaX[columna_independiente].values.reshape(-1, 1)
        y = columnaY.values

        # Ajustar el modelo de regresión lineal
        modelo = LinearRegression()
        modelo.fit(X, y)

        # Visualizar el modelo de regresión lineal simple con colores diferenciados
        colores = plt.cm.viridis(y / y.max())
        plt.scatter(X, y, c=colores, s=100, label='Datos')
        plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Regresión Lineal')

        plt.title(f'Regresión entre {columnaY.name} y {columna_independiente}')
        plt.xlabel(columna_independiente)
        plt.ylabel(columnaY.name)
        plt.legend()
        plt.show()


# Ejemplo de uso:
# Supongamos que df_dependiente es el DataFrame con la variable dependiente
# y df_independientes es el DataFrame con las variables independientes
# regresion_entre_variables(df_dependiente['VariableDependiente'], df_independientes)
