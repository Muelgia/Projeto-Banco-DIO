import numpy as np

A = np.array([[3, 4 ,9], [4, 2, -3], [1, 5, -5]])
B = np.array([[12, -6, 7], [3, 0, 2], [-1, 10, 1]])

C = A * B
print(C)

C = np.matmul(A, B)
print(C)