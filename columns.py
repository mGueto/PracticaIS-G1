import pandas as pd
from read_files import *
from lineal_model import entrenar_modelo_regresion, graficar_prediccion

def select_columns(df: pd.DataFrame) -> tuple:
    """Input:
    df: DataFrame
        Output:
    tuple: variables X, variable Y """
    error = True
    while error: #If a column is entered incorrectly, it will ask again
        print("Lista de columnas del dataFrame: ", df.columns)
        columns_x = input("Escribe el nombre de las columnas para las variables independientes separadas por espacios: ").split() #there can be many x, so use split to add n columns in a list. 
        column_y = input("Escribe el nombre de la columna para la variable dependiente: ") 
        if column_y in df.columns:
            error = False 
            for column_x in columns_x: # check that all columns of x are entered correctly
                if column_x not in df.columns: 
                    error = True 
                    print("\n Se ha producido un error al introducir el nombre de las columnas \n")
        else:
            print("\n Se ha producido un error al introducir el nombre de las columnas \n")
    return columns_x, column_y


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

    columnasX, columnaY = select_columns(dataFrameCSV)

    model, X, y = entrenar_modelo_regresion(dataFrameCSV, columnasX, columnaY)
    # Suponiendo que ya tienes el modelo de regresión 'modelo_regresion' y los datos 'X' y 'y'
    graficar_prediccion(model, X, y)
