import pandas as pd
from read_files import readCSV, readExcel


def selectColumns(df: pd.DataFrame) -> tuple:
    """Input:
    df: DataFrame
        Output:
    tuple: variables X, variable Y """
    error = True 
    while error: #menu loop. If a column is entered incorrectly, it will ask again
        print("--------------------")
        print("Lista de columnas del dataFrame: ", df.columns)
        columnY = input("Escribe el nombre de la columna para la variable dependiente: ") 
        if columnY in df.columns:
            columnsX = input("Escribe el nombre de las columnas para las variables independientes separadas por espacios: ").split() #there can be many x, so use split to add n columns in a list. 
            error = columnsX == [] # if the input are only spaces or nothing, error = True; else, assert error = False unless a column doesn't belong to the input (checked in the next loop)
            for columnX in columnsX: # check that all columns of x are entered correctly
                if columnX not in df.columns: 
                    error = True 
                    print("\n Se ha producido un error al introducir el nombre de las columnas \n")
        else:
            print("\n Se ha producido un error al introducir el nombre de las columnas \n") 
    return df[columnsX], df[columnY]


#Testing
if __name__ == "__main__":
    
    dataFrameCSV = readCSV("housing.csv")

    columnX, columnY = selectColumns(dataFrameCSV)

    print(columnX, '|', columnY)
   
    
    dataFrameExcel = readExcel("housing.xlsx")

    columnX, columnY = selectColumns(dataFrameExcel)

    print(columnX, '|', columnY)
   