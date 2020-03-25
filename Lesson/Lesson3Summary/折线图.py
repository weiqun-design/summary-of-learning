from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

x = [1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910]
y = [265, 323, 136, 220, 305, 350, 419, 450, 560, 720, 830]
plt.plot(x, y)
plt.show()

df = pd.DataFrame({'x': x, "y": y})
sns.lineplot(x="x", y="y", data=df)
plt.show()
