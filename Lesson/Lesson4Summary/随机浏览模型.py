import numpy as np

a = np.array([[0, 1 / 2, 1, 0],
              [1 / 3, 0, 0, 1 / 2],
              [1 / 3, 0, 0, 1 / 2],
              [1 / 3, 1 / 2, 0, 0]])
b = np.array([1 / 4, 1 / 4, 1 / 4, 1 / 4])
w = b

d = 0.85
for i in range(100):
    w = (1-d)/len(b) + d * np.dot(a, w)
    print(w)
