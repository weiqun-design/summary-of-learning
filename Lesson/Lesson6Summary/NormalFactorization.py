import numpy as np
A = np.array([[5, 3],
              [1, 1]])
lamda, U = np.linalg.eig(A)
print(A)
print(lamda)
print(U)