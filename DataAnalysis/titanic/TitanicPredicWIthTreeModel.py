import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import tree

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

pd.set_option('display.max_columns',None)
# print(train_data.info())
# print(train_data.describe())
# print(train_data.describe(include=["O"]))
print(train_data.head(20))

train_data['Age'].fillna(train_data['Age'].mean(),inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)

train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)

print(train_data['Embarked'].value_counts())
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]

dict_vectorizer = DictVectorizer(sparse=False)
train_features = dict_vectorizer.fit_transform(train_features.to_dict(orient='record'))
print(dict_vectorizer.feature_names_)

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(train_features,train_labels)

test_features = dict_vectorizer.fit_transform(test_features.to_dict(orient='record'))
predict_labels = clf.predict(test_features)

print(np.mean(cross_val_score(clf,train_features,train_labels,cv=10)))
with open('output.dot','w') as f:
    f = tree.export_graphviz(clf,out_file=f)
