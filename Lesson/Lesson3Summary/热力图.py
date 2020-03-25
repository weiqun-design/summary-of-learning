import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(33)
data = np.random.rand(3, 3)
print(data)
heatmap = sns.heatmap(data)
plt.show()