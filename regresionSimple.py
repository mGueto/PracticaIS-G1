from class_customModel import CustomModel

def regresionSimpleModel(columnaX, columnaY):
    x = columnaX.values
    y = columnaY.values
    modelo = CustomModel()
    modelo.fit(x, y)
    
    

    return modelo