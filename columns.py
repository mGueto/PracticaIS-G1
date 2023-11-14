import pandas as pd
from read_files import *
from lineal_model import entrenar_modelo_regresion, graficar_prediccion

def select_columns(df: pd.DataFrame) -> tuple:
    """Input:
    df: DataFrame
        Output:
    numCols: pandas.Index"""
    numCols = df.select_dtypes(include=['int64', 'float64']).columns
    print(type(numCols))
    return numCols

#Testing
if __name__ == "__main__":
    """
    print("--------------------")
    dataFrameCSV = readCSV("housing.csv")

    columnasX, columnaY = select_columns(dataFrameCSV)

    print(columnasX, '|', columnaY)
   """
    print("--------------------")
    dataFrameCSV = readCSV("data/housing.csv")

    columnasX = select_columns(dataFrameCSV)

    """model, X, y = entrenar_modelo_regresion(dataFrameCSV, columnasX, columnaY)
    # Suponiendo que ya tienes el modelo de regresión 'modelo_regresion' y los datos 'X' y 'y'
    graficar_prediccion(model, X, y)"""
