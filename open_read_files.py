import pickle

def openArchive(path):
    with open(path) as archivoBiblioteca:
        archive = archivoBiblioteca.readlines()
        for line in archive:
            separatorOfData(line)
            
            
def separatorOfData(line: str):
    data = line.split(" ")
    print(data)

# Más o menos esto ya te lee archivos y te los imprime por pantalla en caso de que sean textos,
# a la hora de meter los datos es parecido. 
# Simplemente sería en vez de imprimirlos guardarlos en algún sitio

def saveText(textSave):
    with open('openReadFiles/readme.txt', 'w') as f:
        f.write(textSave)

saveText("sample text, this could be something like '2x+1; 53' being the first parameter the function and the other one the variance")

openArchive("openReadFiles/readme.txt")

# Ahora a guardar datos xD

class ObjToSave():
    """
    OBJETO DE PRUEBA
    simplemente para probar a guardar objetos
    """
    def __init__(self, x, y, variance) -> None:
        self.x = x
        self.y = y
        self.variance = variance
    
    def imprimirVariance(self):
        print(self.variance)

def saveObject(path, obj):
    with open(path, "wb") as f:
        pickle.dump(obj, f)

objeto = ObjToSave(1, 2, 5)

saveObject("openReadFiles/savedObj.pickle", objeto)


def loadObject(path):
    with open(path, "rb") as file:
        obj = pickle.load(file)
    print(obj.x, obj.y, obj.variance)

loadObject("openReadFiles/savedObj.pickle")

