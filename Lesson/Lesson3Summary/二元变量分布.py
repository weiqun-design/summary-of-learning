import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
print(flights)
sns.jointplot(x="year", y="passengers", data=flights, kind='scatter')  # 散点图
sns.jointplot(x="year", y="passengers", data=flights, kind='kde')  # 核密度图
sns.jointplot(x="year", y="passengers", data=flights, kind="hex")  # hex图
plt.show()

sns.pairplot(flights)
plt.show()