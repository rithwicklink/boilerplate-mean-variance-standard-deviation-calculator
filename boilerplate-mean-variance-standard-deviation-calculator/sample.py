import numpy as np
matrix = [0,1,2,3,4,5,6,7,8]
# print(matrix)
matrix_np = np.reshape(matrix, (3, 3))
print(matrix_np)
sample_print = {'mean' : [[np.min(matrix_np,axis = 0)]],}
print(sample_print)
resultList = list(sample_print.items())
# print(resultList)
# print(np.mean(matrix_np,axis = 1))
# print()
# sum = np.sum(matrix_np)
# print(sum)
# def calculate(list):
#     matrix = np.array([list])



#     return calculations