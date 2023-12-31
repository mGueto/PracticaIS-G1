import sys
sys.path.append('../')  # Agrega la ruta del directorio principal

import pandas as pd
import numpy as np
import pytest
from classCustomModel import CustomModel
from regressionModels import *
from sklearn.metrics import mean_squared_error

# Función para generar datos de prueba
def generate_test_data(size=100):
    np.random.seed(42)
    x_values = np.random.rand(size)
    y_values = 2 * x_values + 1 + 0.1 * np.random.randn(size)
    return pd.DataFrame({'X': x_values, 'Y': y_values})


# Prueba unitaria para multiple_regression_model
def test_multiple_regression_model():
    # Genera datos de prueba
    data = generate_test_data()
    x_columns = data[['X']]
    y_column = data['Y']

    # Llama a la función
    model = multiple_regression_model(x_columns, y_column)

    # Realiza una predicción
    y_pred = model.predict(x_columns)

    # Verifica que la predicción tenga el mismo tamaño que los valores reales
    assert len(y_pred) == len(y_column)

    # Verifica la calidad del modelo (en este caso, usando el error cuadrático medio)
    mse = mean_squared_error(y_column, y_pred)
    assert mse < 0.1, f"Error cuadrático medio demasiado alto: {mse}"

# Ejecutar las pruebas
if __name__ == "__main__":
    pytest.main([__file__])
