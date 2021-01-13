from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error



# class RegreessionInterface:
#     def method1(self, path: str, file_name: str) -> str:
#          """method description"""
#         pass

#     def method2(self, full_file_name: str) -> dict:
#         """method description"""
#         pass
    

#metrics

def show_metrics(y_true, y_pred):
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_absolute_error(y_true, y_pred)
    return r2, mae, mse
    
    
