import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
data = np.random.normal(size=(10, 4))
labels = ['A', 'B', 'C', 'D']
plt.boxplot(data,labels=labels)
plt.show()

df = pd.DataFrame(data, columns=labels)
sns.boxplot(data=df)
plt.show()
