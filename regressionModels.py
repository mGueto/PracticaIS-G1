from classCustomModel import CustomModel

def simple_regression_model(column_x, column_y):
    x = column_x.values
    y = column_y.values
    model = CustomModel()
    model.fit(x, y)
    return model

def multiple_regression_model(columns_x, column_Y):
    x = columns_x
    y = column_Y 
    
    model = CustomModel()   # Training
    model.fit(x, y)
    
    return model