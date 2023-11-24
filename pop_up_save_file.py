from tkinter import *
from tkinter import filedialog
import shutil

def save_file():
    window = Tk()
    window.withdraw()

    # the model must be saved before
    model_to_save = "data/model.pkl"

    if model_to_save:
        destination_file = filedialog.asksaveasfilename(title="Guardar archivo como")

        if destination_file:
            shutil.copy(model_to_save, destination_file + '.pkl')




save_file()