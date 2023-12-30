import pandas as pd
import pytest
from seleccionar_columnas import seleccion_columnas

def test_seleccion_columnas():
    # Crea un DataFrame de prueba
    data = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'target': [7, 8, 9]
    })

    # Llama a la función
    x, y = seleccion_columnas(data)

    # Realiza tus aserciones
    assert isinstance(x, list)
    assert isinstance(y, str)

# Ejecuta las pruebas con pytest
# En la terminal: pytest nombre_del_archivo.py