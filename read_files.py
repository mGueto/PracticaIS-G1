import pandas as pd

def readCSV(path:str) -> pd.DataFrame:
    """Input: 
    path: CSV file path
       Output: 
    Pandas dataframe """
    return pd.read_csv(path)

def readExcel(path:str) -> pd.DataFrame:
    """Input: 
    path: excel file path
       Output: 
    Pandas dataframe """
    return pd.read_excel(path)


if __name__ == "__main__":
    dataFrameCSV = readCSV("housing.csv")

    print(dataFrameCSV)

    dataFrameEXCEL = readExcel("housing.xlsx")

    print(dataFrameEXCEL)