import numpy as np
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

y = np.array([1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0])
scores = np.array([0.9, 0.8, 0.7, 0.6, 0.55, 0.54, 0.53, 0.52, 0.51, 0.505, 0.4, 0.39, 0.38,0.37, 0.36,0.35,0.34,0.33,0.30,0.1])
fpr, tpr, threholds = metrics.roc_curve(y,scores,pos_label=1)
auc = metrics.auc(fpr,tpr)
print(auc)
print(fpr, tpr, threholds)
plt.figure(1)
plt.plot(fpr, tpr)
plt.show()