import numpy as np


def find_fit(x, y, f):
    X = np.array([f(i) for i in x])
    return np.linalg.inv(X.T @ X) @ X.T @ y