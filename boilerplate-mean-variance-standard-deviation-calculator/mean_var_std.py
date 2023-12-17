import numpy as np

def calculate(list):
    matrix_np = np.reshape(list, (3, 3))
    mean_axis_0 = np.mean(matrix_np,axis = 0)
    mean_axis_1 = np.mean(matrix_np,axis = 1)
    mean_f = np.mean(matrix_np) 
    var_axis_0 = np.var(matrix_np,axis = 0)
    var_axis_1 = np.var(matrix_np,axis = 1)
    var_f = np.var(matrix_np)
    max_axis_0 = np.max(matrix_np,axis = 0)
    max_axis_1 = np.max(matrix_np,axis = 1)
    max_f = np.max(matrix_np)
    min_axis_0 = np.min(matrix_np,axis = 0)
    min_axis_1 = np.min(matrix_np,axis = 1)
    min_f = np.min(matrix_np)
    sum_axis_0 = np.sum(matrix_np,axis = 0)
    sum_axis_1 = np.sum(matrix_np,axis = 1)
    sum_f = np.sum(matrix_np)
    calculations = {
        'Mean' : [[mean_axis_0],[mean_axis_1],[mean_f]],
        'Variance' : [[var_axis_0],[var_axis_1],[var_f]],
        'Max' : [[max_axis_0],[max_axis_1],[max_f]],
        'Min' : [[min_axis_0],[min_axis_1],[min_f]],
        'Sum' : [[sum_axis_0],[sum_axis_1],[sum_f]],
    }


    return calculations