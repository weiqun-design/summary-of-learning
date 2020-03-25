import numpy as np

a = np.array([[0, 12, np.inf, np.inf, np.inf, 16, 14],
              [12, 0, 10, np.inf, np.inf, 7,np.inf],
              [np.inf, 10, 0, 3, 5, 6, np.inf],
              [np.inf, np.inf, 3, 0, 4, np.inf, np.inf],
              [np.inf, np.inf, 5, 4, 0, 2, 8],
              [16, 7, 6, np.inf, 2, 0, 9],
              [14, np.inf, np.inf, np.inf, 8, 9, 0]])

n = len(a[0])
for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            if a[i][k] + a[k][j] < a[i][j]:
                a[i][j] = a[i][k] + a[k][j]
print(a)
