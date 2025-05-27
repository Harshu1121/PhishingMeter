from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import numpy as np
import json
import dump

X_train = np.load('../dataset/X_train.npy')
y_train = np.load('../dataset/y_train.npy')

clf = RandomForestClassifier()
print("Cross Validation Score:", cross_val_score(clf, X_train, y_train, cv=10).mean())

clf.fit(X_train, y_train)

X_test = np.load('../dataset/X_test.npy')
y_test = np.load('../dataset/y_test.npy')
pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

json.dump(dump.forest_to_json(clf), open('../../static/classifier.json', 'w'))
