from regresionModels import *
import streamlit as st



def createModel(data, x, y):

        X_mediana = data[x].median()
        Y_mediana = data[y].median()
        data[x] = data[x].fillna(X_mediana)
        data[y] = data[y].fillna(Y_mediana)
        x, y = data[x], data[y]
        
        if x.shape[1] == 1:
            modelo = regresionSimpleModel(x, y)
            

            
        else:
            modelo = regresionMultipleModel(x, y)
            

        
        st.write(modelo)
        return modelo   