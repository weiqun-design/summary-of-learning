import numpy as np
import pandas as pd
import sys
sys.path.append('..')
from sklearn.cluster import KMeans
from sklearn import preprocessing

data = pd.read_csv('team_cluster_data.csv',encoding='GBK')
print(data.head(5))
features = ['2019国际排名','2018世界杯排名','2015亚洲杯排名']
train_x = data[features]
k_means = KMeans(n_clusters=4)
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
print(train_x)
k_means.fit(train_x)
predict_y = k_means.predict(train_x)
print(predict_y)
print(type(predict_y))
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'}, axis=1,inplace=True)
print(result)






