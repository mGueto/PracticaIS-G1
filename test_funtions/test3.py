import pandas as pd
import pytest
from modelos import crearModelo, modelo_regresion_simple, modelo_regresion_multiple
from class_customModelo import CustomModelo
from streamlit.testing.v1 import AppTest

def test_crearModelo_regresion_multiple_con_valores_nulos():
    data = pd.DataFrame({'x1': [1, 2, 3], 'x2': [2, None, 6], 'y': [3, 6, 9]})
    modelo = crearModelo(data, ['x1', 'x2'], 'y')

    # Reemplaza esta línea con las propiedades específicas que deseas verificar en tu modelo
    assert isinstance(modelo, CustomModelo)
    # O verifica alguna propiedad específica de tu modelo en lugar de isna()

# Ajusta según la estructura y propiedades de tu modelo personalizado