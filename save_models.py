import streamlit as st
import pickle


def save_object(path, obj):
    with open(path, "wb") as f:
        pickle.dump(obj, f)

def downloadButton(model):
    try:
        save_object("model_to_save.pickle", model)
        with open("model_to_save.pickle", "rb") as file:
            st.download_button(
                    label="Descargar modelo",
                    data=file,
                    file_name="model.pickle",
                    mime="pickle/pickle")
        st.write("Se ha guardado correctamente el modelo. ¡Revise descargas!")
    except:
        st.write("¡Error! No se puedo guardar el modelo")