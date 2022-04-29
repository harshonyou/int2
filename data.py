import numpy as np

import matplotlib.pyplot as plt
from tensorflow.keras import datasets

from sklearn.model_selection import train_test_split

def getDataset():
    return datasets.cifar10.load_data()

def xNeutralizer(X_data):
    Neutralizer = lambda img : np.mean(img, axis=2)/255
    X_update = np.ndarray(shape=(len(X_data), 32, 32))
    for i in range(len(X_data)):
        X_update[i] = Neutralizer(X_data[i])
    return X_update

def yNeutralizer(y_data):
    y_update = np.ndarray(shape=(len(y_data), 10))
    for i in range(len(y_data)):
        y_update[i][y_data[i]] = 1
    return y_update

def getTrainningDataset():
    (_X_train, _y_train), (_, _) = getDataset()
    X_train = xNeutralizer(_X_train)
    y_train = yNeutralizer(_y_train)
    return X_train, y_train

def getTestingDataset():
    (_, _), (_X_test, _y_test) = getDataset()
    X_test = xNeutralizer(_X_test)
    y_test = yNeutralizer(_y_test)
    return X_test, y_test

def load_data():
    (X_train, y_train) = getTrainningDataset()
    (X_test, y_test) = getTestingDataset()

    X_train, X_valid = train_test_split(X_train, test_size=0.2, random_state=42)
    y_train, y_valid = train_test_split(y_train, test_size=0.2, random_state=42)

    return (X_train, y_train), (X_valid, y_valid), (X_test, y_test)

if __name__ == "__main__":
    (X_train, y_train), (X_valid, y_valid), (X_test, y_test) = load_data()
    print(
        f"Dataset: Train: {len(X_train)} - Valid: {len(X_valid)} - Test: {len(X_test)}")
