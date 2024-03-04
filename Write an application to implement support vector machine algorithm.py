import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# Data Source
datasrc = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
DS = pd.read_csv(datasrc, names=colnames)

# Data Splitting
P = DS.drop('Class', axis=1)
Q = DS['Class']
P_train, P_test, Q_train, Q_test = train_test_split(P, Q, test_size=0.20)

# Polynomial Kernel
print("\nPolynomial Kernel")
degree = 8
classifierp = SVC(kernel='poly', degree=degree)
classifierp.fit(P_train, Q_train)
Q_pred = classifierp.predict(P_test)
print("Confusion Matrix:")
print(confusion_matrix(Q_test, Q_pred))
print("\nClassification Report:")
print(classification_report(Q_test, Q_pred))

# Gaussian Kernel
print("\nGaussian Kernel")
classifierg = SVC(kernel='rbf')
classifierg.fit(P_train, Q_train)
Q_pred = classifierg.predict(P_test)
print("Confusion Matrix:")
print(confusion_matrix(Q_test, Q_pred))
print("\nClassification Report:")
print(classification_report(Q_test, Q_pred))

# Sigmoid Kernel
print("\nSigmoid Kernel")
classifiers = SVC(kernel='sigmoid')
classifiers.fit(P_train, Q_train)
Q_pred = classifiers.predict(P_test)
print("Confusion Matrix:")
print(confusion_matrix(Q_test, Q_pred))
print("\nClassification Report:")
print(classification_report(Q_test, Q_pred))
