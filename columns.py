import pandas as pd
from read_files import *
from lineal_model import entrenarModeloRegresion, graficarPrediccion

import pandas as pd

def selectColumns(df: pd.DataFrame) -> tuple:
    """Input:
    df: DataFrame
        Output:
    tuple: variables X, variable Y """
    error = True
    while error: #If a column is entered incorrectly, it will ask again
        print("Lista de columnas del dataFrame: ", df.columns)
        columnsX = input("Escribe el nombre de las columnas para las variables independientes separadas por espacios: ").split() #there can be many x, so use split to add n columns in a list. 
        columnY = input("Escribe el nombre de la columna para la variable dependiente: ") 
        if columnY in df.columns:
            error = False 
            for columnX in columnsX: # check that all columns of x are entered correctly
                if columnX not in df.columns: 
                    error = True 
                    print("\n Se ha producido un error al introducir el nombre de las columnas \n")
        else:
            print("\n Se ha producido un error al introducir el nombre de las columnas \n")
    return columnsX, columnY

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

    columnasX, columnaY = selectColumns(dataFrameCSV)

    model, X, y = entrenarModeloRegresion(dataFrameCSV, columnasX, columnaY)
    # Suponiendo que ya tienes el modelo de regresión 'modeloRegresion' y los datos 'X' y 'y'
    graficarPrediccion(model, X, y)