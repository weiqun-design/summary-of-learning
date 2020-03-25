from matplotlib import pyplot as plt
import seaborn as sns

x = ['c1', 'c2', 'c3', 'c4']
y = [15, 18, 5, 26]
plt.bar(x, y)
plt.show()

sns.barplot(x, y)
plt.show()