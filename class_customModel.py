from sklearn.linear_model import LinearRegression
from pandas import *

class CustomModel(LinearRegression):
    def __init__(self, X_columns = None, y_columns = None):
        super().__init__()
        self.X_columns = X_columns
        self.y_columns = y_columns

    def set_data(self, X_columns, y_columns):
        self.X_columns = X_columns
        self.y_columns = y_columns

    def get_independent_variable_names(self):
        return self.X_columns[:]

    def get_dependent_variable_name(self):
        return self.y_columns.name