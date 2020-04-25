from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

N = 500
x = np.random.randn(N)
y = np.random.randn(N)

plt.scatter(x, y, marker='x')
plt.show()
df = pd.DataFrame({'x': x, 'y': y})
sns.jointplot(x='x', y='y', data=df, kind='scatter')
plt.show()