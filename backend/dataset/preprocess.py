import arff
import numpy as np
import json
from sklearn.model_selection import train_test_split

# Load dataset
dataset = arff.load(open('dataset.arff', 'r'))
data = np.array(dataset['data'])

# Select useful features
data = data[:, [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 22, 30]]

X, y = data[:, :-1], data[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Save data
np.save('X_train.npy', X_train)
np.save('X_test.npy', X_test)
np.save('y_train.npy', y_train)
np.save('y_test.npy', y_test)

test_data = {"X_test": X_test.tolist(), "y_test": y_test.tolist()}
with open('../../static/testdata.json', 'w') as tdfile:
    json.dump(test_data, tdfile)
