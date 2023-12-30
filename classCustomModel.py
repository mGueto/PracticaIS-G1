from sklearn.linear_model import LinearRegression
from pandas import *

class CustomModel(LinearRegression):
    def __init__(self, columns_x = None, columns_y = None):
        super().__init__()
        self.columns_x = columns_x
        self.columns_y = columns_y

    def set_data(self, columns_x, columns_y):
        self.columns_x = columns_x
        self.columns_y = columns_y

    def get_independent_variable_names(self):
        return self.columns_x[:]

    def get_dependent_variable_name(self):
        return self.columns_y.name