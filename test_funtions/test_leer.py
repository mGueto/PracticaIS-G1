import unittest
from unittest.mock import MagicMock
from leer_archivos import leer_archivos

class TestLeerArchivos(unittest.TestCase):
    def setUp(self):
        # Puedes usar MagicMock para simular el comportamiento de los métodos de lectura
        self.mock_csv_reader = MagicMock()
        self.mock_excel_reader = MagicMock()
        self.mock_sql_reader = MagicMock()

    def test_leer_archivos_csv(self):
        uploaded_file = MagicMock(name="test_data/housing.csv")
        uploaded_file.name.endswith.return_value = True
        with unittest.mock.patch('leer_archivos.readCSV', self.mock_csv_reader):
            result = leer_archivos(uploaded_file)
        self.mock_csv_reader.assert_called_once_with(uploaded_file)
        # Aquí verifica que la función devuelva lo esperado


if __name__ == '__main__':
    unittest.main()
