import sys
sys.path.append('../')  # Agrega la ruta del directorio principal

import pandas as pd
from modelOperations import create_model
from classCustomModel import CustomModel

def test_create_model_regresion_multiple():
    data = pd.DataFrame({'x1': [1, 2, 3], 'x2': [2, None, 6], 'y': [3, 6, 9]})
    modelo = create_model(data, ['x1', 'x2'], 'y')

    assert isinstance(modelo, CustomModel)

def test_create_model_regresion_simple():
    data = pd.DataFrame({'x1': [1, 2, 3], 'y': [3, 6, 9]})
    modelo = create_model(data, ['x1'], 'y')

    assert isinstance(modelo, CustomModel)
