from readFile import _readCSV, _readExcel, _readSQL
from columns import *


#Las funciones internas son privadas ya que solo se usan dentro de esa función
def ReadFiles(uploaded_file):

    if uploaded_file.name.endswith('.csv'):
        data = _readCSV(uploaded_file) 
    elif uploaded_file.name.endswith('.xlsx'):
        data = _readExcel(uploaded_file)
    else:
        uploaded_file.name.endswith('.bd')
        data = _readSQL(uploaded_file) 
        
    return data