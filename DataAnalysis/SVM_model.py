from sklearn import svm
model_1 = svm.LinearSVC()  # 线性分类器，仅只能使用线性核函数
model_2 = svm.SVC(kernel='rbf', C=1.0, gamma='auto')