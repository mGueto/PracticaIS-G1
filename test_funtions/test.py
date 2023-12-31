import pytest
from read_files import readCSV, readExcel, readSQL
from streamlit.testing.v1 import AppTest
from leer_archivos import *
from io import BytesIO

class TestReadDataFunctions:

    def test_readCSV(self):
        # Supone que 'test_data.csv' es un archivo de prueba en el directorio de pruebas
        df = readCSV('test_data/housing.csv')
        assert df is not None  # Verifica que se obtiene un DataFrame
        assert not df.empty  # Verifica que el DataFrame no está vacío

    def test_readExcel(self):
        # Supone que 'test_data.xlsx' es un archivo de prueba en el directorio de pruebas
        df = readExcel('test_data/housing.xlsx')
        assert df is not None  # Verifica que se obtiene un DataFrame
        assert not df.empty  # Verifica que el DataFrame no está vacío

    def test_readSQL(self):
        # Crea un objeto BytesIO que simula un archivo cargado
        with open('test_data/housing.db', 'rb') as f:  # Asegúrate de que este archivo exista
            mock_uploaded_file = BytesIO(f.read())

        # Llama a la función readSQL con el objeto BytesIO
        df = readSQL(mock_uploaded_file)

        # Realiza tus aserciones aquí
        assert df is not None
        assert not df.empty
        # Puedes añadir más aserciones para verificar detalles específicos de los datos cargados
    
    def test_leer_archivos(self):
        # Crea un objeto BytesIO que simula un archivo cargado
        with open('test_data/housing.db', 'rb') as f:  # Asegúrate de que este archivo exista
            mock_uploaded_file = BytesIO(f.read())

        df = leer_archivos(mock_uploaded_file)
        assert df is not None
        assert not df.empty


# Si quieres ejecutar las pruebas desde la línea de comandos, puedes usar:
# pytest -v nombre_del_archivo.py
