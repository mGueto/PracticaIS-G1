import matplotlib.pyplot as plt
import streamlit as st

def plot_model(model, column_x, column_y):
    if column_x.shape[1] == 1:
        x, y = column_x.values, column_y.values
        
        plt.scatter(x, y, c = 'blue', s = 100, label = 'Datos')
        plt.plot(x, model.predict(x), color = 'red', linewidth = 2, label = 'Regresión Lineal')
        plt.title('Modelo de Regresión Lineal Simple')
        plt.xlabel(column_x.columns[0])
        plt.ylabel(column_y.name)
        plt.legend()
        st.pyplot(plt)
    
    else: 
        x = column_x
        y = column_y
        quotients = model.coef_
        intercept = model.intercept_

        for i, column in enumerate(x.columns):
                predictions = intercept + quotients[i] * x[column]
                
                plt.scatter(x[column], y, label=f'Datos')
                plt.plot(x[column], predictions, label = f'Predicción ({column})', color = 'red')
                plt.xlabel(column)
                plt.ylabel(y.name)  # Asumes df_y has one column only
                plt.legend()
                plt.show()
                st.pyplot(plt)
                plt.clf()