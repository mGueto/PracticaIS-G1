import pandas as pd
from modelOperations import create_model
from classCustomModel import CustomModel

def test_create_model_regresion_multiple_con_valores_nulos():
    data = pd.DataFrame({'x1': [1, 2, 3], 'x2': [2, None, 6], 'y': [3, 6, 9]})
    modelo = create_model(data, ['x1', 'x2'], 'y')

    # Reemplaza esta línea con las propiedades específicas que deseas verificar en tu modelo
    assert isinstance(modelo, CustomModel)
    # O verifica alguna propiedad específica de tu modelo en lugar de isna()

# Ajusta según la estructura y propiedades de tu modelo personalizado