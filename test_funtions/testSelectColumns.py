import sys
sys.path.append('../')  # Agrega la ruta del directorio principal

import pandas as pd
import pytest
from selectColumns import select_columns

def test_seleccion_columnas():
    # Crea un DataFrame de prueba
    data = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'target': [7, 8, 9]
    })

    # Llama a la función
    numeric_columns = select_columns(data)

    # Realiza tus aserciones
    assert isinstance(numeric_columns, (list, pd.Index)), "numeric_columns debe ser una lista o un pandas.Index"
    
    # Si numeric_columns es un Index, conviértelo a una lista para las siguientes aserciones
    if isinstance(numeric_columns, pd.Index):
        numeric_columns = numeric_columns.tolist()

    # Verifica que todas las columnas en numeric_columns son del tipo numérico
    for col in numeric_columns:
        assert col in data.columns, f"La columna {col} no está en el DataFrame original"
        assert pd.api.types.is_numeric_dtype(data[col]), f"La columna {col} no es de tipo numérico"
    #Develve un index de Pandas

# Ejecuta las pruebas con pytest
# En la terminal: pytest nombre_del_archivo.py