from numpy.core.fromnumeric import mean
import numpy as np
from sklearn.metrics import mean_squared_log_error

def rmsle(y_pred,y_true):
    return np.sqrt(mean_squared_log_error(y_pred,y_true))
