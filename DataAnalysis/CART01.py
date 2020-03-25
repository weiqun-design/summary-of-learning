from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data
labels = iris.target
for i in range(150):
    print(str(labels[i]) + ": " + str(features[i]))
train_features, test_features, train_lebels, test_labels = train_test_split(features, labels,test_size=0.33, random_state=0)
clf = DecisionTreeClassifier(criterion="gini")
clf.fit(train_features, train_lebels)
test_predict = clf.predict(test_features)
score = accuracy_score(test_labels, test_predict)
with open('out.dot','w') as f:
    f = tree.export_graphviz(clf, out_file=f)
print("准确率 '{0}'".format(score))
