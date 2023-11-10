import pickle

def open_archive(path):
    with open(path) as archivo_biblioteca:
        archive = archivo_biblioteca.readlines()
        for line in archive:
            separator_of_data(line)
            
            
def separator_of_data(line:str):
    data = line.split(" ")
    print(data)

#más o menos esto ya te lee archivos y te los imprime por pantalla en caso de que sean textos,
# a la hora de meter los datos es parecido. 
# Simplemente sería en vez de imprimirlos guardarlos en algún sitio

def save_text(text_save):
    with open('open_read_files/readme.txt', 'w') as f:
        f.write(text_save)

save_text("sample text, this could be something like '2x+1; 53' being the first parameter the function and the other one the variance")

open_archive("open_read_files/readme.txt")

#ahora a guardar datos xD

class obj_to_save():
    """
    OBJETO DE PRUEBA
    simplemente para probar a guardar objetos
    """
    def __init__(self, x, y, varianza) -> None:
        self.x = x
        self.y = y
        self.varianza = varianza
    
    def imprimir_varianza(self):
        print(self.varianza)

def save_object(path, obj):
    with open(path, "wb") as f:
        pickle.dump(obj, f)

objeto = obj_to_save(1,2, 5)

save_object("open_read_files/saved_obj.pickle", objeto)


def load_object(path):
    with open(path, "rb") as file:
        obj = pickle.load(file)
    print(obj.x,obj.y,obj.varianza)

load_object("open_read_files/saved_obj.pickle")

